from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response
import time
import random

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter("hello_request_total", "Total number of /hello requests")

# Gauge: 当前活跃连接数（可增可减的值）
active_connections = Gauge("active_connections", "Current number of active connections")

# Histogram: 请求处理时间分布（按桶统计）
request_duration_seconds = Histogram(
    "request_duration_seconds",
    "Request duration in seconds",
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0],  # 定义时间桶
)

# Summary: 请求延迟（自动计算百分位数）
request_latency_seconds = Summary(
    "request_latency_seconds", "Request latency in seconds"
)


# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
