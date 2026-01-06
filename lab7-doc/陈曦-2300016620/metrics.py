from prometheus_client import Counter, Gauge, Histogram, Summary, generate_latest
from flask import Response

# 1) Counter: 单调递增计数器，适合记录请求总数、错误总数等
# Prometheus 查询示例：
#   - 总量： hello_request_total
#   - 速率： rate(hello_request_total[1m]) 或 increase(hello_request_total[5m])
hello_counter = Counter(
    "hello_request_total",
    "Total number of /hello requests"
)

# 2) Gauge: 可增可减的即时数值，适合记录当前并发、队列长度或任意瞬时值
# Prometheus 查询示例： app_random_gauge 或 avg_over_time(app_random_gauge[5m])
app_random_gauge = Gauge(
    "app_random_gauge",
    "A gauge that changes value on each /hello request"
)

# 3) Histogram: 记录值分布，Prometheus 会导出 bucket/count/sum，可用 histogram_quantile 计算分位数
# 导出序列示例：
#   app_request_duration_seconds_bucket{le="..."}
#   app_request_duration_seconds_count
#   app_request_duration_seconds_sum
# Prometheus 查询示例（P95）：
#   histogram_quantile(0.95, sum(rate(app_request_duration_seconds_bucket[5m])) by (le))
request_duration_histogram = Histogram(
    "app_request_duration_seconds",
    "Histogram of simulated request durations"
)

# 4) Summary: 记录延迟的汇总（客户端可计算 quantiles），Prometheus 导出 count/sum
# 查询示例：
#   app_request_latency_seconds_count
#   app_request_latency_seconds_sum
request_latency_summary = Summary(
    "app_request_latency_seconds",
    "Summary of simulated request latencies"
)


# 暴露所有 metrics
def metrics():
    return Response(generate_latest(), mimetype="text/plain")
