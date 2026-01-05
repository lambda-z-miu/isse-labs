from flask import Flask
from metrics import (
    hello_counter,
    active_connections,
    request_duration_seconds,
    request_latency_seconds,
    metrics,
)
import time
import random

app = Flask(__name__)


@app.route("/hello")
def hello():
    # Counter: 增加访问计数
    hello_counter.inc()

    # Gauge: 模拟活跃连接数变化（随机增加或减少）
    change = random.choice([-1, 0, 1, 1])  # 倾向于增加
    if change > 0:
        active_connections.inc(change)
    elif change < 0:
        active_connections.dec(abs(change))

    # Histogram: 记录请求处理时间
    start_time = time.time()
    # 模拟一些处理时间（0.05 到 2 秒之间）
    processing_time = random.uniform(0.05, 2.0)
    time.sleep(processing_time)
    elapsed = time.time() - start_time
    request_duration_seconds.observe(elapsed)

    # Summary: 记录请求延迟
    request_latency_seconds.observe(elapsed)

    return f"Hello World! (Processing time: {elapsed:.3f}s)"


@app.route("/simulate")
def simulate():
    """模拟端点，用于快速生成指标变化"""
    # 随机增加活跃连接数
    active_connections.inc(random.randint(1, 5))

    # 记录一个随机处理时间
    duration = random.uniform(0.1, 3.0)
    request_duration_seconds.observe(duration)
    request_latency_seconds.observe(duration)

    return f"Simulated request (Duration: {duration:.3f}s)"


@app.route("/reset")
def reset():
    """重置 Gauge 值（用于测试）"""
    active_connections.set(0)
    return "Active connections reset to 0"


# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
