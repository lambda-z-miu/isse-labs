from flask import Flask
from metrics import hello_counter, current_online_users, wait_time_histogram, request_time_summary, metrics
import time
import random

app = Flask(__name__)

@app.route("/hello")
def hello():
    hello_counter.inc()

    change = random.choice([-2, -1, 1, 2]) # 随机增加或减少在线用户数
    current_online_users.inc(change)

    start_time = time.time()
    wait_time = random.uniform(0.01, 0.5)
    time.sleep(wait_time)
    end_time = time.time()
    duration = end_time - start_time
    wait_time_histogram.observe(duration)
    request_time_summary.observe(duration)


    return (
        f"Hello World! "
        f"| Counter Incremented. "
        f"| Gauge changed by {change}. "
        f"| Process Time: {duration:.4f}s recorded by Hist & Summary."
    )

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
