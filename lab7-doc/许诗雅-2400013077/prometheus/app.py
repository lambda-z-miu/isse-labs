from flask import Flask
import time
import random
from metrics import hello_counter, cpu_usage_gauge, request_latency_histogram, request_size_summary, metrics

app = Flask(__name__)

@app.route("/hello")
def hello():
    # 1. Counter: 增加计数
    hello_counter.inc()
    
    # 2. Gauge: 随机设置 CPU 使用率 (0-100)
    cpu_usage_gauge.set(random.uniform(0, 100))
    
    # 3. Histogram: 记录请求耗时
    start_time = time.time()
    # 模拟业务处理耗时 (0.05s - 0.6s)
    time.sleep(random.uniform(0.05, 0.6))
    duration = time.time() - start_time
    request_latency_histogram.observe(duration)
    
    # 4. Summary: 记录请求/响应大小 (模拟字节数)
    request_size_summary.observe(random.randint(100, 5000))
    
    return "Hello World!"

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
