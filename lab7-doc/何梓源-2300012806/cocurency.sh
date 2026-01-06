#!/usr/bin/env bash

# 并发 8 线程请求 /work，默认各执行 20 次
COUNT=${1:-20}

seq "$COUNT" | xargs -n1 -P8 -I{} curl -s http://localhost:8000/work >/dev/null
echo "Done: ${COUNT} requests with 8 concurrent workers."