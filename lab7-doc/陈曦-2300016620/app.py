from flask import Flask
from metrics import (
    hello_counter,
    metrics,
    app_random_gauge,
    request_duration_histogram,
    request_latency_summary,
)
import random
import time

app = Flask(__name__)

@app.route("/hello")
def hello():
    """主业务路由：每次访问会触发所有示例指标的变化

    - `hello_counter`: 计数器 +1
    - `app_random_gauge`: 随机设值（0-100）
    - `request_duration_histogram` / `request_latency_summary`: 记录随机时延
    """
    # 计数器
    hello_counter.inc()

    # 随机设置 Gauge 的值
    app_random_gauge.set(random.randint(0, 100))

    # 模拟处理耗时（0.01 - 0.5 秒），记录到 histogram 与 summary
    duration = random.uniform(0.01, 0.5)
    time.sleep(duration)
    request_duration_histogram.observe(duration)
    request_latency_summary.observe(duration)

    return "Hello World!"

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
