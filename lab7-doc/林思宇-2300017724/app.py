import random
import time

from flask import Flask

from metrics import (
    hello_counter,
    hello_processing_seconds_histogram,
    hello_processing_seconds_last,
    hello_processing_seconds_summary,
    metrics,
)

app = Flask(__name__)

@app.route("/hello")
def hello():
    start = time.perf_counter()
    time.sleep(random.uniform(0.05, 0.3))
    elapsed = time.perf_counter() - start

    hello_counter.inc()
    hello_processing_seconds_last.set(elapsed)
    hello_processing_seconds_histogram.observe(elapsed)
    hello_processing_seconds_summary.observe(elapsed)
    return "Hello World!"

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
