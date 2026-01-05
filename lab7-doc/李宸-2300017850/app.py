from flask import Flask
import random
import time
from metrics import hello_counter, hello_gauge, hello_histogram, hello_summary, metrics

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/hello")
def hello():
    # 1. Counter: 增加计数
    hello_counter.inc()
    
    # 2. Gauge: 设置一个随机值 (0-100)
    random_val = random.randint(0, 100)
    hello_gauge.set(random_val)
    
    # 模拟处理时间
    process_time = random.uniform(0.1, 0.5)
    time.sleep(process_time)
    
    # 3. Histogram: 记录处理时间
    hello_histogram.observe(process_time)
    
    # 4. Summary: 记录处理时间
    hello_summary.observe(process_time)
    
    return "Hello World!"

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
