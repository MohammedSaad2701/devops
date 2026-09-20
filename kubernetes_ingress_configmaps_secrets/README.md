# Kubernetes Ingress, ConfigMaps, and Secrets

This lab runs a frontend and backend behind one NGINX Ingress:

```text
yatri.local/      -> Frontend Service -> NGINX Pods
yatri.local/api/  -> Backend Service  -> Python Pods
```

Apply all resources with:

```bash
kubectl apply -f .
kubectl get pods,services,ingress
```

## ConfigMap

The ConfigMap stores non-sensitive settings such as the environment, log level, port, currency, and booking limit. Both workloads load these values without rebuilding their images.

```bash
kubectl get configmap yatri-app-config -o yaml
```

## Secret

The Secret is intended for database values such as the username, password, and database name. Secret data is Base64 encoded, not encrypted, so real credentials should be managed outside committed YAML files.

```bash
kubectl get secret yatri-db-secret
```

Do not print Secret values in screenshots or documentation.

## Ingress

The NGINX Ingress provides one host-based entry point. `/` goes to the frontend, while `/api/` goes to the backend. The rewrite rule removes the `/api` prefix before the request reaches the backend.

```bash
kubectl get ingress yatri-ingress
curl -H 'Host: yatri.local' http://<ingress-address>/
curl -H 'Host: yatri.local' http://<ingress-address>/api/
```

## Evidence

The screenshots show the deployed ingress routes and the application responses.

![Ingress routes](screenshots/Screenshot%202026-09-20%20at%206.18.16%E2%80%AFPM.png)

![Application responses](screenshots/Screenshot%202026-09-20%20at%206.18.23%E2%80%AFPM.png)

## Takeaway

ConfigMaps hold ordinary application settings, Secrets separate sensitive values from code, and Ingress exposes multiple Services through one host and path-based entry point.
