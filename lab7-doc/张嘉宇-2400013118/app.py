from flask import Flask, jsonify
from metrics import hello_counter, active_users, request_duration, processing_time, metrics
import random
import time

app = Flask(__name__)

@app.route("/hello")
def hello():
    # 记录请求开始时间用于Histogram统计
    start_time = time.time()
    
    hello_counter.inc()
    
    # 模拟处理时间变化，让Histogram有数据
    processing_delay = random.uniform(0.1, 2.0)
    time.sleep(processing_delay)
    
    # 记录请求持续时间
    request_duration.observe(time.time() - start_time)
    
    return "Hello World!"

@app.route("/users/login")
def user_login():
    """模拟用户登录，增加活跃用户数"""
    # 随机增加1-5个活跃用户
    increment = random.randint(1, 5)
    active_users.inc(increment)
    return jsonify({"message": f"User logged in. Active users increased by {increment}"})

@app.route("/users/logout")
def user_logout():
    """模拟用户登出，减少活跃用户数"""
    # 随机减少1-3个活跃用户，但不能小于0
    decrement = random.randint(1, 3)
    current_value = active_users._value._value
    if current_value >= decrement:
        active_users.dec(decrement)
    else:
        active_users.set(0)
    return jsonify({"message": f"User logged out. Active users decreased by {decrement}"})

@app.route("/process")
def process_data():
    """模拟数据处理，用于Summary指标统计"""
    # 使用Summary的timer装饰器来测量处理时间
    with processing_time.time():
        # 模拟不同的处理时间
        processing_delay = random.uniform(0.5, 3.0)
        time.sleep(processing_delay)
        
    return jsonify({"message": "Data processed successfully", "duration": f"{processing_delay:.2f}s"})

@app.route("/status")
def status():
    """返回当前系统状态"""
    return jsonify({
        "message": "System is running",
        "current_active_users": active_users._value._value,
        "total_hello_requests": hello_counter._value._value
    })

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 初始化一些活跃用户
    active_users.set(random.randint(10, 50))
    
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
