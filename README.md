docker run --name pg-docker -e POSTGRES_USER=speedtest -e POSTGRES_DB=speedtest -e POSTGRES_PASSWORD=speedtest -d postgres

172.18.0.2


django:
gunicorn -w 4 -b localhost:8080 djangospeed.wsgi

flask:
gunicorn -w 4 -b localhost:8090 app:app


docker run --rm williamyeh/wrk
docker run --rm  -v `pwd`:/data williamyeh/wrk -c1 -t1 -d5s -s benchmark/test_script.lua "http://localhost:8090"






sudo apt-get install parallel
sudo apt-get install apache2-utils


ab -n 100 -c 10 http://localhost:8080/speedtest/simple


https://github.com/tortoise/orm-benchmarks