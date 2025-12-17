from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response

# 定义一个计数器，用于统计 /hello 的访问次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests",
)

gauge = Gauge(
    "random_number_query",
    "Randomized value",
)

hist = Histogram(
    "random_number_hist",
    "Collection of random numbers",
    buckets=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
)

summary = Summary(
    "random_number_summary",
    "Summary of random numbers",
)

# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
