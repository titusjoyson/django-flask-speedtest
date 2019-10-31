#!/bin/bash
echo "" > benchmark/results/flask_result_ob.txt
input="benchmark/urls/flask.txt"
while IFS= read -r line
do
  ab -n 1000 -c 10 "$line" >> benchmark/results/flask_result_ob.txt
  echo "" >> benchmark/results/flask_result_ob.txt
done < "$input"
ab -n 1000 -c 10 -p benchmark/data/create.json -T 'application/json' http://127.0.0.1:8080/speedtest/create >> benchmark/results/flask_result_ob.txt
echo "" >> benchmark/results/flask_result_ob.txt
ab -n 1000 -c 10 -u benchmark/data/update.json -T 'application/json' http://127.0.0.1:8080/speedtest/save >> benchmark/results/flask_result_ob.txt
echo "" >> benchmark/results/flask_result_ob.txt
ab -n 1000 -c 10 -u benchmark/data/update.json -T 'application/json' http://127.0.0.1:8080/speedtest/update >> benchmark/results/flask_result_ob.txt
echo "" >> benchmark/results/flask_result_ob.txt