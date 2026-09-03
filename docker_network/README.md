# Docker networking exercises

This README documents a short 3-tier Docker networking exercise and some verification steps (commands and expected behavior).

## Overview

- Create separate bridge networks for frontend, backend, and database services.
- Run containers attached to those networks and verify inter-container connectivity.
- Demonstrate a host bind mount to serve a simple static page from a container.

## Useful commands

Create networks:

```sh
docker network create frontend-net
docker network create backend-net
docker network create database-net
```

List networks:

```sh
docker network ls
```

Run example containers (replace or adapt images as needed):

```sh
# frontend (nginx)
docker run -d --name frontend --network frontend-net nginx

# backend (alpine interactive or your backend image)
docker run -d --name backend --network backend-net alpine sleep 1d

# database (mysql example)
docker run -d --name database --network database-net -e MYSQL_ROOT_PASSWORD=example mysql:8.0
```

Verify processes and ports:

```sh
docker ps
```

Verify connectivity from one container to another (example: from `backend`):

```sh
docker exec backend ping -c 3 frontend
docker exec backend ping -c 3 database
```

The expected result is successful ICMP replies showing that containers on their respective bridge networks can reach the target containers by name or IP (as shown in the exercise screenshots).

## Bind mount example (serve a local file via nginx)

Create a host folder and a simple `index.html`:

```sh
mkdir -p ~/docker-bind
echo "Hello students - Docker Bind Mount" > ~/docker-bind/index.html
```

Run an nginx container that serves the bind-mounted file:

```sh
docker run -d --name bind-nginx -p 8080:80 -v ~/docker-bind:/usr/share/nginx/html:ro nginx
```

Open http://localhost:8080 in a browser — you should see the content of `index.html` (e.g. "Hello students - Docker Bind Mount").

## Notes and verification

- Sample outputs captured during the exercise include `docker network ls`, `docker ps`, ping results between containers, and browser screenshots showing the served pages.
- If you use different image names or ports adjust the commands above accordingly.

If you want, I can copy the terminal screenshots into this folder and reference them from the README for visual documentation.

## Screenshots

Below are references to screenshots captured during the exercise. The images are stored in the `screenshots/` folder.

- Network listing: ![network-ls](screenshots/01-network-ls.png)
- Running containers (`docker ps`): ![docker-ps](screenshots/02-docker-ps.png)
- Ping/connectivity results: ![ping-results](screenshots/03-ping-results.png)
- Apache default page: ![apache-it-works](screenshots/04-apache-it-works.png)
- Bind-mount creation and host file: ![bind-create](screenshots/05-bind-mount-create.png)
- Bind-mount served page in browser: ![bind-browser](screenshots/06-bind-mount-browser.png)

