# Docker Images and Multi-stage Builds

This example uses a Node.js application to demonstrate Docker image builds, containers, and a multi-stage Dockerfile.

## Build and run

From the `multi_stage_app/` directory:

```bash
docker build -t multi-stage-hello .
docker run -d --name multi-stage-hello -p 8080:3000 multi-stage-hello
curl http://localhost:8080
```

The current example also needs a `FROM node:24-alpine AS builder` stage and a `package.json` file before the build command can run successfully.

Expected application response:

```text
Hello World from Docker multi-stage build
```

## Multi-stage idea

The builder stage installs the Node.js dependencies. The production stage copies only the application files and dependencies, runs as the non-root `node` user, and exposes port `3000`.

Useful image commands:

```bash
docker images
docker ps
docker logs multi-stage-hello
```

The screenshots show the Docker run error when the image has not been built locally, followed by container and bind-mount output from the exercise.

![Docker image and run output](Screenshot%202026-09-03%20at%2010.14.19%E2%80%AFPM.png)

![Container output and application response](Screenshot%202026-09-03%20at%2010.14.26%E2%80%AFPM.png)

## Takeaway

Build the image before running it. Multi-stage builds keep build steps separate from the smaller production image.

