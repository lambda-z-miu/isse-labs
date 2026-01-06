import random
import time

from flask import Flask
from metrics import (
    hello_counter,
    hello_inprogress,
    hello_latency_histogram,
    hello_latency_summary,
    metrics,
)

app = Flask(__name__)

@app.route("/hello")
def hello():
    start_time = time.perf_counter()
    with hello_inprogress.track_inprogress():
        hello_counter.inc()
        simulated_delay = random.uniform(0.05, 0.3)  # add small jitter so latency metrics change
        time.sleep(simulated_delay)
        elapsed = time.perf_counter() - start_time
        hello_latency_histogram.observe(elapsed)
        hello_latency_summary.observe(elapsed)
    return "Hello World!"

app.add_url_rule("/metrics", "metrics", metrics)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
