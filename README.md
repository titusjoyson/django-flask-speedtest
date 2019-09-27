### How to rerun the test ?

```
# build and run the containers
docker-compose up --build -d

# lets load some data

# loginto django container
docker-compose exec django bash

django# cd djangospeed
# this will insert 10000 records
django# python manage.py load_data 10000
django# exit

# this will create the results in side 
# benchmark/results/flask_docker_result_ob.txt
# benchmark/results/django_docker_result_ob.txt
bash benchmark/run_test_docker.sh
```

### Local setup
```
sudo apt-get install apache2-utils
```
todo: WIP
