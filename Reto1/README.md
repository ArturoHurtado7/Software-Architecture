# CCS central API 

first challenge, create a central API to manage the CCS central with 2 quality attributes:

- **Performance**:
    - **Latency**: the API must be able to handle 5000 requests per second
    - **Scalability**: the API must be able to handle (5000 requests per second) * 5 minutes from 50 to 5000 requests per second

## Run the API
to run localy use the following command

uvicorn main:app --host 0.0.0.0 --port 8000 --reload