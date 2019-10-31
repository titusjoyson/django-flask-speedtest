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
Time taken for tests:   2.579 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      4278000 bytes
HTML transferred:       3820000 bytes
Requests per second:    775.60 [#/sec] (mean)
Time per request:       12.893 [ms] (mean)
Time per request:       1.289 [ms] (mean, across all concurrent requests)
Transfer rate:          1620.13 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       4
Processing:     3   13  34.1     10     513
Waiting:        3   13  34.1     10     513
Total:          3   13  34.1     10     513

Percentage of the requests served within a certain time (ms)
  50%     10
  66%     11
  75%     11
  80%     12
  90%     13
  95%     15
  98%     18
  99%     20
 100%    513 (longest request)
```

### ORM Benchmarking

Time taken to complete 1000 queries:

|  Action    | Django ORM  | Flask-SQLAlchemy  |
|------------|-------------|-------------------|
| Select     | 0.032263662 |       0.012180415 |
| Count      | 1.403982088 |        2.63598253 |
| pagination | 4.687958269 |        3.82162432 |
| aggregate  | 2.005817666 |       2.569968947 |
| create     | 3.228642431 |       4.362719425 |
| save       | 4.824882885 |       1.669172032 |
| update     | 3.277724468 |        5.25546317 |

## Reference

- A better ORM Comparison [link](https://github.com/tortoise/orm-benchmarks)

## Support

Please [open an issue](https://github.com/titusjoyson/django-flask-speedtest/issues/new) for support.

## Contributing

Please contribute by Creating a branch, adding commits, and [open a pull request](https://github.com/titusjoyson/django-flask-speedtest/compare/).

