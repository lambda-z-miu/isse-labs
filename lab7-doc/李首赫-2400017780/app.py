from flask import Flask, g
from metrics import hello_counter, active_users, request_duration_histogram, request_duration_summary, metrics
import time

app = Flask(__name__)

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    if hasattr(g, 'start_time'):
        duration = time.time() - g.start_time
        request_duration_histogram.observe(duration)
        request_duration_summary.observe(duration)
    return response

@app.route("/hello")
def hello():
    hello_counter.inc()
    return "Hello World!"

@app.route("/login")
def login():
    active_users.inc()
    return "Logged in!"

@app.route("/logout")
def logout():
    active_users.dec()
    return "Logged out!"

# 暴露 Prometheus 指标
app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    # 让服务可以被 Docker 访问
    app.run(host="0.0.0.0", port=8000)
