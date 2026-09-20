# Docker Networking

This lab demonstrates Docker bridge networks, container communication, and a host bind mount served by NGINX.

## 1. Create the networks

```bash
docker network create frontend-net
docker network create backend-net
docker network create database-net
docker network ls
```

Each network separates one application tier. Containers must share a network before they can resolve each other by name.

![Docker networks](screenshots/Screenshot%202026-09-03%20at%206.58.34%E2%80%AFPM.png)

## 2. Run the containers

```bash
docker run -d --name frontend --network frontend-net nginx
docker run -d --name backend --network backend-net alpine sleep 1d
docker run -d --name database --network database-net \
	-e MYSQL_ROOT_PASSWORD=example mysql:8.0
```

Connect the backend to the other tiers so it can reach them:

```bash
docker network connect frontend-net backend
docker network connect database-net backend
docker ps
```

![Running containers](screenshots/Screenshot%202026-09-03%20at%206.59.05%E2%80%AFPM.png)

## 3. Test container communication

```bash
docker exec backend ping -c 3 frontend
docker exec backend ping -c 3 database
```

Successful replies confirm that Docker DNS and the shared network connections are working.

![Container connectivity](screenshots/Screenshot%202026-09-03%20at%207.00.21%E2%80%AFPM.png)

## 4. Bind mount with NGINX

The `bind_mount/index.html` file is mounted into an NGINX container, so changes on the host are visible in the container.

```bash
docker run -d --name bind-nginx -p 8080:80 \
	-v "$PWD/bind_mount:/usr/share/nginx/html:ro" nginx
```

Open [http://localhost:8080](http://localhost:8080) to view the mounted page.

![Bind-mount file](screenshots/Screenshot%202026-09-03%20at%207.04.06%E2%80%AFPM.png)

![NGINX default page](screenshots/Screenshot%202026-09-03%20at%207.05.32%E2%80%AFPM.png)

![Updated bind-mount page](screenshots/Screenshot%202026-09-03%20at%207.05.50%E2%80%AFPM.png)

![Bind-mount browser result](screenshots/Screenshot%202026-09-03%20at%207.06.02%E2%80%AFPM.png)

![Final network list](screenshots/Screenshot%202026-09-03%20at%207.06.38%E2%80%AFPM.png)

## Takeaway

Docker networks control container communication, while bind mounts share files between the host and a container.

