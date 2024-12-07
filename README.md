# GIFT SHAKER
(Fast modifications to prepare app for my family and Christmas)
## Gift Shaker is the app for anyone who wants to shake up emails with friends or family and create an extra gift party

### We have two options:

* [dev version](#dev)
* [develop version with gunicorn](#prod)

### And what should we do

* [ TODO ](#todo)

I have a lot of work to do on this project, but this is the version we can see and work with this app.
We have a postgres database and a django project packed in docker-compose. I set variables in env files and make them
available (yes, I know, we don't do this in the real world) hearing to give the possibilities of using this application
as simple as possible on our computers.

<a name="dev"></a>
### To run develop version
```shell
docker-compose -f docker-compose.yml up --build
```
[Register site](http://127.0.0.1:8080/login/register/)

##

<a name="prod"></a>
### To run production version
```shell
docker-compose -f docker-compose.prod.yaml up --build
```
[Register site](http://127.0.0.1:8000/login/register/)

##

#### To set local environment and use .env.dev file
```shell
set -o allexport; source .env.dev; set +o allexport
```



# TESTS
```shell
set -o allexport; source .env.dev; set +o allexport
```
```shell
export DJANGO_SETTINGS_MODULE=gifts_shaker.settings
```


# CONTAINERS
### Get into postgres container
```shell
docker exec -it gifts_shaker-db-1  psql -U giftshaker_dev
```
<a name="todo"></a>
### TODO

&#x2713; delete shaker option
&#x2713; permissions to buttons

+ better frontend
+ tests
+ to correct docker-compose on production
+ ...
