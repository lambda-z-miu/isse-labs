from flask import Response
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest

# Counter: /hello 请求次数
hello_counter = Counter("hello_request_total", "Total number of /hello requests")

# Gauge: 最近一次 /hello 的处理耗时（秒）
hello_processing_seconds_last = Gauge(
    "hello_processing_seconds_last",
    "Processing time (seconds) of the latest /hello request",
)

# Histogram: /hello 处理耗时分布（秒）
hello_processing_seconds_histogram = Histogram(
    "hello_processing_seconds_histogram",
    "Histogram of /hello processing time in seconds",
    buckets=(0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2, 2.0),
)

# Summary: /hello 处理耗时汇总（秒）
hello_processing_seconds_summary = Summary(
    "hello_processing_seconds_summary",
    "Summary of /hello processing time in seconds",
)


def metrics():
    return Response(generate_latest(), mimetype="text/plain")
