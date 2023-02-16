# CCS central API 

first challenge, create a central API to manage the CCS central with 2 quality attributes:

- **Performance**:
    - **Latency**: the API must be able to handle 5000 requests per second
    - **Scalability**: the API must be able to handle (5000 requests per second) * 5 minutes from 50 to 5000 requests per second

## Run the API
to run localy use the following command

virtual environment
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

## docker
- show containers:
    docker ps
- enter command line:
    docker exec -it ccs_back /bin/bash
- stop container:
    docker stop ccs_back
- start container:
    docker-compose up -d
- rebuild container:
    docker-compose up --force-recreate --build -d
- logs
    docker-compose logs -f

## API documentation
http://localhost:8000/docs#/


