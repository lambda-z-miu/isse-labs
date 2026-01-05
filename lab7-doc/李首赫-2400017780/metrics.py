from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

# 定义一个Gauge，用于统计活跃用户数
active_users = Gauge(
    "active_users_total",
    "Number of active users"
)

# 定义一个Histogram，用于统计请求持续时间
request_duration_histogram = Histogram(
    "request_duration_seconds",
    "Request duration in seconds",
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0]
)

# 定义一个Summary，用于统计请求持续时间
request_duration_summary = Summary(
    "request_summary_seconds",
    "Request duration summary in seconds"
)

# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
