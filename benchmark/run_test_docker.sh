#!/bin/bash
echo "" > benchmark/results/flask_docker_result_ob.txt
input="benchmark/urls/docker_flask.txt"
while IFS= read -r line
do
  ab -n 2000 -c 10 "$line" >> benchmark/results/flask_docker_result_ob.txt
done < "$input"
ab -n 2000 -c 10 -p benchmark/data/create.json -T 'application/json' http://127.0.0.1:8000/flask/speedtest/create >> benchmark/results/flask_docker_result_ob.txt
ab -n 2000 -c 10 -u benchmark/data/update.json -T 'application/json' http://127.0.0.1:8000/flask/speedtest/save >> benchmark/results/flask_docker_result_ob.txt
ab -n 2000 -c 10 -u benchmark/data/update.json -T 'application/json' http://127.0.0.1:8000/flask/speedtest/update >> benchmark/results/flask_docker_result_ob.txt

echo "" > benchmark/results/django_docker_result_ob.txt
input="benchmark/urls/docker_django.txt"
while IFS= read -r line
do
  ab -n 2000 -c 10 "$line" >> benchmark/results/django_docker_result_ob.txt
done < "$input"
ab -n 2000 -c 10 -p benchmark/data/create.json -T 'application/json' http://127.0.0.1:8000/django/speedtest/create/ >> benchmark/results/django_docker_result_ob.txt
ab -n 2000 -c 10 -u benchmark/data/update.json -T 'application/json' http://127.0.0.1:8000/django/speedtest/save/ >> benchmark/results/django_docker_result_ob.txt
ab -n 2000 -c 10 -u benchmark/data/update.json -T 'application/json' http://127.0.0.1:8000/django/speedtest/update/ >> benchmark/results/django_docker_result_ob.txt