import random
import time

from flask import Flask
from metrics import (
    hello_counter,
    metrics,
    record_work_metrics,
    work_inprogress_gauge,
)

app = Flask(__name__)

@app.route("/hello")
def hello():
    hello_counter.inc()
    return "Hello World!"


@app.route("/work")
def work():
    # 模拟一个需要处理时间的请求，并记录指标
    sleep_time = random.uniform(0.02, 0.6)
    with work_inprogress_gauge.track_inprogress():
        start = time.perf_counter()
        time.sleep(sleep_time)
        duration = time.perf_counter() - start

    response = f"work done in {duration:.3f}s\n"
    record_work_metrics(duration, response)
    return response

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
