# Dummy Task App

## Requirements

```
pip install -r requirements.txt
```

## Run endpoint locally

### Server
In the root folder of the project run the following command:

```
uvicorn main:app --reload
```
or
```
python3 -m uvicorn main:app --reload
```

### Client
1. Create
    `curl -X POST -H "Content-Type: application/json" -d '{"title": "Task 3", "description": "This is task 3"}' http://127.0.0.1:8000/tasks`
2. Retrieve
    `curl http://127.0.0.1:8000/tasks`
    `curl http://127.0.0.1:8000/tasks/{task_id}`
3. Update
    `curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task 1", "description": "This task has been updated", "status": "complete"}' http://127.0.0.1:8000/tasks/{task_id}`
4. Delete
    `curl -X DELETE http://127.0.0.1:8000/tasks/{task_id}`



## Docker

- Docker build
  ```sh
  docker build --pull --rm -f $PWD/docker/Dockerfile -t task_app .
  ```
- Docker run
  - interactive
    ```sh
    docker run -it --rm --privileged --network=host --name task_app-container task_app
    ```
  - main
    ```sh
    docker run -it --rm --privileged --network=host --name task_app-container task_app python3 -m uvicorn main:app --reload
    ```
- Docker tag
    ```sh
    docker tag task_app:latest 602586604912.dkr.ecr.us-east-1.amazonaws.com/task_app:latest
    ```
- Docker push
    ```sh
    docker push 602586604912.dkr.ecr.us-east-1.amazonaws.com/task_app:latest
    ```
- Clean
  ```sh
  docker image prune -f && docker container prune -f && docker system prune -f
  ```


## AWS integration

- AWS API Gateway
- AWS Secret Manager
- AWS Lambda
- AWS ECR/ECS


### Preconditions

#### Packing

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp main.py deployment/
cp -r venv/lib/python3.10/site-packages/* deployment/

cd deployment/
zip -r app.zip .
mv app.zip ../
```


### Client

- Get
    curl https://4prpoob6s2xt2zepzhf3tbytku0mmlov.lambda-url.us-east-1.on.aws/tasks
    curl https://khd7eoccj0.execute-api.us-east-1.amazonaws.com/develop/TaskAppFunction/tasks

