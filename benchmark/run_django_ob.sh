#!/bin/bash
echo "" > benchmark/results/django_result_ob.txt
input="benchmark/urls/django.txt"
while IFS= read -r line
do
  ab -n 1000 -c 10 "$line" >> benchmark/results/django_result_ob.txt
  echo "" >> benchmark/results/django_result_ob.txt
done < "$input"
ab -n 1000 -c 10 -p benchmark/data/create.json -T 'application/json' http://127.0.0.1:8090/speedtest/create/ >> benchmark/results/django_result_ob.txt
echo "" >> benchmark/results/django_result_ob.txt
ab -n 1000 -c 10 -u benchmark/data/update.json -T 'application/json' http://127.0.0.1:8090/speedtest/update/ >> benchmark/results/django_result_ob.txt
echo "" >> benchmark/results/django_result_ob.txt