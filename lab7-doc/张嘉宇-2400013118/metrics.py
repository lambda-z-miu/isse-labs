from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response
import random
import time

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

# 定义一个Gauge，用于模拟当前活跃用户数
active_users = Gauge(
    "active_users_current",
    "Current number of active users"
)

# 定义一个Histogram，用于统计请求响应时间
request_duration = Histogram(
    "request_duration_seconds",
    "Request duration in seconds",
    buckets=(0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0)
)

# 定义一个Summary，用于统计数据处理时间
processing_time = Summary(
    "processing_time_seconds",
    "Time spent processing data"
)

# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
