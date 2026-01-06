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
    hello_counter.inc()
    
    # Gauge
    random_val = random.randint(0, 100)
    hello_gauge.set(random_val)
    
    process_time = random.uniform(0.1, 0.5)
    time.sleep(process_time)
    
    # Histogram
    hello_histogram.observe(process_time)
    
    # Summary
    hello_summary.observe(process_time)
    
    return f"Hello World! (Value: {random_val}, Time: {process_time:.4f}s)"

app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
