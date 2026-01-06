from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

current_online_users = Gauge(
    "app_online_users",
    "Current number of online users"
)

WAIT_TIME_BUCKETS = (0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, float('inf'))
wait_time_histogram = Histogram(
    "app_wait_time_seconds_hist",
    "Histogram of wait time in seconds",
    buckets=WAIT_TIME_BUCKETS
)

request_time_summary = Summary(
    "app_request_time_seconds_summary",
    "Summary of request process time in seconds"
)

# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
