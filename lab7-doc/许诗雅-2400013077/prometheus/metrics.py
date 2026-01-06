from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

# Gauge: 模拟 CPU 使用率 (数值可升可降)
cpu_usage_gauge = Gauge(
    "cpu_usage_percent",
    "Current CPU usage percentage"
)

# Histogram: 模拟请求延迟 (统计分布情况)
request_latency_histogram = Histogram(
    "request_latency_seconds",
    "Request latency in seconds",
    buckets=[0.1, 0.2, 0.5, 1.0, 2.0] # 自定义桶
)

# Summary: 模拟请求大小 (统计分位数)
request_size_summary = Summary(
    "request_size_bytes",
    "Request size in bytes"
)

# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
