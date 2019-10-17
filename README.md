# Django Vs Flask

A repo for performing speed test, ORM benchmarking and framework comparison with minimal web application setup between Django and Flask. Visit [My article]() for more details.

## Table of Contents

- [Installation](#installation)
- [Run Test](#run-test)
- [Report](#report)
- [Sample Results](#sample-results)
- [Reference](#reference)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Follow the docker [installation guide](https://docs.docker.com/install/) to install docker in your local machine

## Run Test

Clone the Repo and Run the Test:

```sh
git clone https://github.com/titusjoyson/django-flask-speedtest
cd django-flask-speedtest

# build and run the containers
docker-compose up --build -d

# load some data
# login to django container
docker-compose exec django bash
django# cd djangospeed

# insert 10000 records
django# python manage.py load_data 10000
django# exit

# Run the bellow command to create the results in
# benchmark/results/flask_docker_result_ob.txt
# benchmark/results/django_docker_result_ob.txt
bash benchmark/run_test_docker.sh
```

## Sample Results

### Requests/Sec Benchmarking

Check the results [here](https://github.com/titusjoyson/django-flask-speedtest/tree/master/findings)

```
Server Software:        nginx/1.17.4
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /django/speedtest/simple/
Document Length:        1910 bytes

Concurrency Level:      10
Time taken for tests:   0.169 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      213900 bytes
HTML transferred:       191000 bytes
Requests per second:    591.10 [#/sec] (mean)
Time per request:       16.918 [ms] (mean)
Time per request:       1.692 [ms] (mean, across all concurrent requests)
Transfer rate:          1234.72 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     2   16   3.6     16      22
Waiting:        2   16   3.6     16      22
Total:          3   16   3.6     16      22

Percentage of the requests served within a certain time (ms)
  50%     16
  66%     18
  75%     19
  80%     19
  90%     20
  95%     21
  98%     22
  99%     22
 100%     22 (longest request)
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/
```

### ORM Benchmarking

Time taken to complete 1000 queries:

|   Action   | Django         | Flask sqlalchemy |
|:----------:|----------------|------------------|
| Select     | 0.005555028998 | 0.020545132      |
| Count      | 3.12668605     | 3.417979217      |
| pagination | 3.118750306    | 3.82162432       |
| aggregate  | 4.778394117    | 0.014073401      |
| create     | 8.733365253    | 3.1216882        |
| update     | 3.741050111    | 0.250841299      | 

## Reference

- A better ORM Comparison [link](https://github.com/tortoise/orm-benchmarks)

## Support

Please [open an issue](https://github.com/titusjoyson/django-flask-speedtest/issues/new) for support.

## Contributing

Please contribute by Creating a branch, adding commits, and [open a pull request](https://github.com/titusjoyson/django-flask-speedtest/compare/).

