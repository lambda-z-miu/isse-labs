from flask import Response
from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest

hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests",
)

hello_work_gauge = Gauge(
    "hello_work_factor",
    "A changing gauge set by /hello (demo work factor)",
)

hello_latency_histogram = Histogram(
    "hello_request_latency_seconds",
    "Latency of /hello requests in seconds",
    buckets=(0.05, 0.1, 0.25, 0.5, 1.0, 2.5),
)

hello_latency_summary = Summary(
    "hello_request_latency_summary_seconds",
    "Latency summary of /hello requests in seconds",
)


def metrics():
    return Response(generate_latest(), mimetype="text/plain")
