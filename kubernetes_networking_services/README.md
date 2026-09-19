# Kubernetes Networking and Services

This lab demonstrates five Kubernetes Service types.

## Service overview

| Service type | Scope | Main purpose |
| --- | --- | --- |
| ClusterIP | Internal cluster network | Stable access to a group of Pods |
| NodePort | Node IP and fixed port | Simple external access for local or bare-metal clusters |
| LoadBalancer | External load balancer | Public application access in cloud environments |
| ExternalName | DNS alias only | Internal name for an external service |
| Headless Service | Direct Pod DNS | Discovery of individual Pods in stateful workloads |

## Prerequisites

- A Kubernetes cluster with `kubectl` configured
- Minikube users may need `minikube tunnel` for the LoadBalancer example

## 1. ClusterIP

ClusterIP provides stable internal access to matching NGINX Pods, even when Pod IPs change.

Apply and check the resources:

```bash
kubectl apply -f clusterip/
kubectl get pods,service,endpoints -l lab=kubernetes-services
```

### Screenshots

![ClusterIP resources](clusterip/screenshots/Screenshot%202026-09-19%20at%207.20.51%E2%80%AFPM.png)

![ClusterIP service](clusterip/screenshots/Screenshot%202026-09-19%20at%207.25.02%E2%80%AFPM.png)

![ClusterIP endpoints](clusterip/screenshots/Screenshot%202026-09-19%20at%207.25.21%E2%80%AFPM.png)

![ClusterIP client response](clusterip/screenshots/Screenshot%202026-09-19%20at%207.25.49%E2%80%AFPM.png)

## 2. NodePort

NodePort exposes the application on port `30080` on every cluster node and also provides a ClusterIP.

Apply and access the service:

```bash
kubectl apply -f nodeport/
kubectl get pods,service
minikube service web-service-nodeport --url
```

### Screenshots

![NodePort resources](nodeport/screenshots/Screenshot%202026-09-19%20at%207.30.43%E2%80%AFPM.png)

![NodePort service](nodeport/screenshots/Screenshot%202026-09-19%20at%207.32.28%E2%80%AFPM.png)

![NodePort application](nodeport/screenshots/Screenshot%202026-09-19%20at%207.33.33%E2%80%AFPM.png)

![NodePort response](nodeport/screenshots/Screenshot%202026-09-19%20at%207.33.43%E2%80%AFPM.png)

## 3. LoadBalancer

LoadBalancer exposes matching Pods through an external load balancer. On Minikube, run `minikube tunnel` if the external IP is pending.

Apply the resources:

```bash
kubectl apply -f loadbalancer/
kubectl get pods,service
minikube tunnel
```

### Screenshots

![LoadBalancer resources](loadbalancer/screenshots/Screenshot%202026-09-19%20at%2010.43.54%E2%80%AFPM.png)

![LoadBalancer service](loadbalancer/screenshots/Screenshot%202026-09-19%20at%2010.44.18%E2%80%AFPM.png)

![LoadBalancer external access](loadbalancer/screenshots/Screenshot%202026-09-19%20at%2010.45.43%E2%80%AFPM.png)

## 4. ExternalName

ExternalName maps `external-database-service` to the external host `api.github.com` without selecting Pods.

Apply and test the DNS alias:

```bash
kubectl apply -f externalname/
kubectl get service external-database-service
kubectl exec -it dns-test-client -- nslookup external-database-service
```

### Screenshot

![ExternalName response](externalname/screenshots/Screenshot%202026-09-19%20at%2010.53.40%E2%80%AFPM.png)

## 5. Headless Service

A headless Service uses `clusterIP: None` and returns the individual Pod addresses for direct discovery.

Apply and inspect the Pod DNS records:

```bash
kubectl apply -f headless/
kubectl get pods,service
kubectl exec -it headless-dns-client -- nslookup web-service-headless
```

### Screenshots

![Headless Service resources](headless/screenshots/Screenshot%202026-09-19%20at%2010.58.07%E2%80%AFPM.png)

![Headless Service DNS](headless/screenshots/Screenshot%202026-09-19%20at%2010.59.35%E2%80%AFPM.png)

![Headless Pod discovery](headless/screenshots/Screenshot%202026-09-19%20at%2011.01.18%E2%80%AFPM.png)

![Headless direct Pod response](headless/screenshots/Screenshot%202026-09-19%20at%2011.01.57%E2%80%AFPM.png)

## Takeaway

Use `ClusterIP` internally, `NodePort` for simple node exposure, `LoadBalancer` for public cloud access, `ExternalName` for DNS aliases, and headless Services for stateful Pod discovery.
