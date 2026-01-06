from prometheus_client import Counter, generate_latest, Gauge, Histogram, Summary
from flask import Response

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

# 2. Gauge: 监控当前状态
current_active_users = Gauge("current_active_users", "Current number of active users")

# 3. Histogram: 统计分布
request_latency_histogram = Histogram("request_latency_seconds", "Response latency in seconds")

# 4. Summary: 统计分位数
request_latency_summary = Summary("request_latency_summary_seconds", "Response latency summary")

# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
