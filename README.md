# Approximate Counting in Django and Postgres

## Want to learn how to build this?

Check out the [post](#).

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Spin up a Postgres instance:

    ```sh
    (venv)$ docker run --name ecomm-postgres -p 5432:5432 \
              -e POSTGRES_USER=ecomm -e POSTGRES_PASSWORD=complexpassword123 \
              -e POSTGRES_DB=ecomm -d postgres
    ```
   
    > Alternatively, you can use a locally installed Postgres instance. Just make sure to update the *settings.py* file.

1. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

1. Populate the database:

    ```sh
    (venv)$ python manage.py populate_db
    ```
   
    > To speed up the process, run multiple instances of the command.

1. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```
   
1. Navigate to [http://localhost:8000/admin/](http://localhost:8000/admin/) in your browser. Login as:
    
    ```sh
    username: admin
    password: password
    ```
