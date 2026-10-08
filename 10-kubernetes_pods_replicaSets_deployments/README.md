# Kubernetes Pods, ReplicaSets, and Deployments

This lab demonstrates three Kubernetes workload resources using NGINX.

| Resource | Manifest | Purpose |
| --- | --- | --- |
| Pod | `pods/nginx-pod.yaml` | Runs one NGINX container |
| ReplicaSet | `replicaset/nginx-replicaset.yaml` | Maintains three Pods |
| Deployment | `deployment/nginx-deployment.yaml` | Supports updates and rollback |

## Pod

A Pod is Kubernetes' smallest deployable unit. This standalone Pod runs NGINX with defined resource settings and is not recreated if deleted.

```sh
kubectl apply -f pods/nginx-pod.yaml
kubectl get pod nginx-pod -o wide
```

![Pod creation and running state](<pods/screenshots/Screenshot 2026-09-18 at 7.27.47 PM.png>)

![Pod labels and configuration details](<pods/screenshots/Screenshot 2026-09-18 at 7.30.20 PM.png>)

## ReplicaSet

A ReplicaSet keeps three matching NGINX Pods running and replaces a Pod when one is deleted.

```sh
kubectl apply -f replicaset/nginx-replicaset.yaml
kubectl get pods -l app=nginx-replicaset
kubectl delete pod <pod-name>
kubectl get pods -l app=nginx-replicaset
```

![ReplicaSet creation and Pod count](<replicaset/screenshots/Screenshot 2026-09-18 at 7.33.57 PM.png>)

![ReplicaSet replacing a deleted Pod](<replicaset/screenshots/Screenshot 2026-09-18 at 7.34.31 PM.png>)

## Deployment

A Deployment manages ReplicaSets and provides controlled rolling updates. This example starts three replicas and changes NGINX from version 1.25 to 1.26.

```sh
kubectl apply -f deployment/nginx-deployment.yaml
kubectl rollout status deployment/nginx-deployment
kubectl set image deployment/nginx-deployment nginx=nginx:1.26-alpine
kubectl rollout status deployment/nginx-deployment
kubectl rollout history deployment/nginx-deployment
kubectl rollout undo deployment/nginx-deployment
```

![Deployment creation and initial rollout](<deployment/screenshots/Screenshot 2026-09-18 at 7.43.29 PM.png>)

![Deployment image update and revision history](<deployment/screenshots/Screenshot 2026-09-18 at 7.43.35 PM.png>)

![Deployment rollback](<deployment/screenshots/Screenshot 2026-09-18 at 7.43.47 PM.png>)

## Takeaway

Pods run containers, ReplicaSets maintain Pod counts, and Deployments manage ReplicaSets with safe updates and rollback support.
