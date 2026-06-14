# Assignment 15 - Dockerized Python Application

## Description

This project demonstrates a Dockerized Python application using the official Python 3.12 Slim image.

The application prints:

* Python Version
* Current Date and Time

## Files

```text
Assignment_15_Docker/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── docker_output.png
```

## Docker Image

Base Image:

```dockerfile
python:3.12-slim
```

## Build Image

```bash
docker build -t assignment15 .
```

## Run Container

```bash
docker run assignment15
```

## Sample Output

```text
Python Version: 3.12.13
Current Date and Time: 2026-06-14 11:04:45.405071
```

## Screenshot

See `docker_output.png` for the execution screenshot.
