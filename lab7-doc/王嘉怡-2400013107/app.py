from flask import Flask
import time
import random
from metrics import hello_counter, current_active_users, request_latency_histogram, request_latency_summary, metrics

app = Flask(__name__)

@app.route("/hello")
def hello():
    hello_counter.inc()
    # Gauge: 模拟当前活跃人数波动 (增加或减少)
    current_active_users.set(random.randint(10, 100))
    
    # Histogram & Summary: 记录处理时间
    start_time = time.time()
    
    # 模拟业务逻辑耗时
    time.sleep(random.uniform(0.1, 0.5)) 
    
    duration = time.time() - start_time
    request_latency_histogram.observe(duration)
    request_latency_summary.observe(duration)
    
    return "Hello World!"

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
