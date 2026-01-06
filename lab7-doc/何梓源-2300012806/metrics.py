import random
import time

from flask import Response
from prometheus_client import Gauge, Histogram, Summary, Counter, generate_latest

# 计数器：统计 /hello 请求次数
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests",
)

# Gauge：记录当前正在处理的 /work 请求数
work_inprogress_gauge = Gauge(
    "work_inprogress_gauge",
    "Number of in-progress /work requests",
)

# Histogram：记录 /work 处理时延，使用常见的桶划分
work_latency_seconds = Histogram(
    "work_latency_seconds",
    "Latency for /work handler in seconds",
    buckets=(0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0),
)

# Summary：记录返回内容的字节大小，用来展示分位数
work_response_bytes = Summary(
    "work_response_bytes",
    "Response payload size for /work endpoint in bytes",
)


def record_work_metrics(simulated_work_seconds: float, response_text: str) -> None:
    """更新与 /work 相关的指标。"""
    work_latency_seconds.observe(simulated_work_seconds)
    work_response_bytes.observe(len(response_text.encode("utf-8")))


# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
