from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response

hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

hello_inprogress = Gauge(
    "hello_inprogress_requests",
    "Number of in-progress /hello requests"
)

hello_latency_histogram = Histogram(
    "hello_request_latency_seconds",
    "Histogram of /hello request latency in seconds",
    buckets=(0.05, 0.1, 0.2, 0.3, 0.5, 1.0)
)

hello_latency_summary = Summary(
    "hello_request_latency_seconds_summary",
    "Summary of /hello request latency in seconds"
)

def metrics():
    return Response(generate_latest(), mimetype="text/plain")
