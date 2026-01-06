from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

# 定义一个仪表盘
hello_gauge = Gauge(
    "hello_gauge",
    "A value which can inc or dec"
)

# 定义一个直方图，用于统计请求响应时间的分布
hello_histogram = Histogram(
    "hello_request_response_time",
    "Response time of /hello requests in seconds"
)

# 定义一个摘要，用于统计平均响应时间
hello_summary = Summary(
    "hello_response_time_summary",
    "Response time summary of /hello request"
)

# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
