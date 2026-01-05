from prometheus_client import Counter, generate_latest, Gauge, Histogram, Summary
from flask import Response

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

hello_gauge = Gauge(
    "hello_gauge_metric",
    "A gauge metric for demonstration"
)

hello_histogram = Histogram(
    "hello_histogram_metric",
    "A histogram metric for demonstration"
)

hello_summary = Summary(
    "hello_summary_metric",
    "A summary metric for demonstration"
)

# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
