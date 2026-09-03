# Docker Fundamentals: Hello World Apps

This repository contains simple Hello World web applications built and run with Docker.

## Included apps
- node-app
- python-app
- java-app
- apache-app
- react-app
- nginx-app

## Run locally
Each folder has its own Dockerfile.

Example:

```bash
docker build -t node-hello ./node-app
docker run -d -p 3000:3000 --name node-hello node-hello
curl http://localhost:3000
```
