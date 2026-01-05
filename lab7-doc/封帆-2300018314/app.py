from flask import Flask
import random, time
from metrics import hello_counter, metrics, hello_gauge, hello_histogram, hello_summary

app = Flask(__name__)
@app.route("/hello")
def hello():
    hello_counter.inc()
    hello_gauge.set(random.randint(0,100)) #随机值
    start_time = time.perf_counter()
    time.sleep(random.uniform(0.05,0.25))   
    hello_histogram.observe(time.perf_counter() - start_time)
    hello_summary.observe(time.perf_counter() - start_time)
    return "Hello World!"

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
