#!/usr/bash

for i in {1...50}
do
locust --host="http://localhost:80" --no-web -c "$i" -t 30 2>&1
done