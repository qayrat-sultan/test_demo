# Test Task

Demo for test task

## Postgres Settings 

        $ sudo -i -u postgres
        postgres=# createuser -s -e -d -R -P test_task
        postgres=# createdb -O test_task test_task
> Rename `.env.dist` to `.env`

## Basic Commands for local using

        $ pip install -r requirements/local.txt
        $ python manage.py migrate
        $ python manage.py createsuperuser --username=admin  --email=example@mail.com
        $ python manage.py add_fake_workers --count=50000


#### Running tests with pytest

    $ pytest

    $ python manage.py runserver

> Enjoy using 😉
