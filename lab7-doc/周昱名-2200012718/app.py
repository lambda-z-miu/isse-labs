from flask import Flask
from metrics import hello_counter, hello_gauge, hello_histogram, hello_summary, metrics
import random
import time

app = Flask(__name__)

@app.route("/hello")
def hello():
    hello_counter.inc()

    if random.random() > 0.5:
        hello_gauge.inc()
    else:
        hello_gauge.dec()

    response_time = random.uniform(0.1, 1)
    time.sleep(response_time)

    hello_histogram.observe(response_time)
    hello_summary.observe(response_time)

    return "Hello World!"

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
