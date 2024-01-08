# Dummy Task App


- [Dummy Task App](#dummy-task-app)
  - [Requirements](#requirements)
  - [Local execution](#local-execution)
    - [Requiremnts](#requiremnts)
    - [Run server](#run-server)
    - [Test client](#test-client)
  - [Docker local execution \[Ubuntu base image\]](#docker-local-execution-ubuntu-base-image)
    - [Build dockerimage](#build-dockerimage)
    - [Run server](#run-server-1)
    - [Test client](#test-client-1)
  - [Docker local execution \[AWS base image\]](#docker-local-execution-aws-base-image)
    - [Build dockerimage](#build-dockerimage-1)
    - [Run server](#run-server-2)
    - [Test client](#test-client-2)
  - [AWS \[Lambda + API Gateway\]](#aws-lambda--api-gateway)
    - [Requirements](#requirements-1)
    - [Packing](#packing)
    - [AWS lambda](#aws-lambda)
  - [AWS \[CodeBuild + Lambda + API Gateway\]](#aws-codebuild--lambda--api-gateway)
  - [AWS \[ECS + Lambda + API Gateway\]](#aws-ecs--lambda--api-gateway)


## Requirements

```
pip install -r requirements.txt
```


## Local execution

### Requiremnts

```
pip install -r requirements.txt
```

### Run server

In the root folder of the project run the following command:

```
uvicorn main:app --reload
```
or
```
python3 -m uvicorn main:app --reload
```


### Test client
1. Create
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Task 3", "description": "This is task 3"}' http://127.0.0.1:8000/tasks
    ```
2. Retrieve
    ```sh
    curl http://127.0.0.1:8000/tasks
    curl http://127.0.0.1:8000/tasks/{task_id}
    ```
3. Update
    ```sh
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task 1", "description": "This task has been updated", "status": "complete"}' http://127.0.0.1:8000/tasks/{task_id}
    ```
4. Delete
    ```sh
    curl -X DELETE http://127.0.0.1:8000/tasks/{task_id}
    ```


## Docker local execution [Ubuntu base image]

### Build dockerimage

```sh
docker build --platform linux/amd64 --rm -f $PWD/docker/Dockerfile_ubuntu -t dummy_task_app .
```

```sh
docker image prune -f && docker container prune -f && docker system prune -f
```

### Run server
```sh
docker run -it --rm --privileged -p 8080:8000 --name task_app-container dummy_task_app
python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Test client
1. Create
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Task 3", "description": "This is task 3"}' http://127.0.0.1:8080/tasks
    ```
2. Retrieve
    ```sh
    curl http://127.0.0.1:8080/tasks
    curl http://127.0.0.1:8080/tasks/{task_id}
    ```
3. Update
    ```sh
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task 1", "description": "This task has been updated", "status": "complete"}' http://127.0.0.1:8000/tasks/{task_id}
    ```
4. Delete
    ```sh
    curl -X DELETE http://127.0.0.1:8080/tasks/{task_id}
    ```




## Docker local execution [AWS base image]

### Build dockerimage

```sh
docker build --platform linux/amd64 --rm -f $PWD/docker/Dockerfile -t dummy_task_app .
```

```sh
docker image prune -f && docker container prune -f && docker system prune -f
```

### Run server
```sh
docker run -it --rm --privileged -p 8000:8000 --name task_app-container dummy_task_app
```

### Test client
1. Create
    ```sh
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Task 3", "description": "This is task 3"}' http://127.0.0.1:8000/tasks
    ```
2. Retrieve
    ```sh
    curl http://127.0.0.1:8000/tasks
    curl http://127.0.0.1:8000/tasks/{task_id}
    ```
3. Update
    ```sh
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Task 1", "description": "This task has been updated", "status": "complete"}' http://127.0.0.1:8000/tasks/{task_id}
    ```
4. Delete
    ```sh
    curl -X DELETE http://127.0.0.1:8000/tasks/{task_id}
    ```



## AWS [Lambda + API Gateway]

### Requirements
- Local execution

### Packing

```sh
source packing.sh
```

### AWS lambda
- Creating lambda function
- Load .zip file



## AWS [CodeBuild + Lambda + API Gateway]

- Docker tag
    ```sh
    docker tag dummy_task_app:latest 602586604912.dkr.ecr.us-east-1.amazonaws.com/dummy_task_app:latest
    ```
- Docker push
    ```sh
    docker push 602586604912.dkr.ecr.us-east-1.amazonaws.com/dummy_task_app:latest
    ```


## AWS [ECS + Lambda + API Gateway]


