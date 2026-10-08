# Kubernetes Fundamentals

This lab introduces Kubernetes cluster architecture, `kubectl`, and namespaces.

| Topic | Directory | Purpose |
| --- | --- | --- |
| Cluster architecture | `cluster_architecture/` | View control plane and node components |
| `kubectl` basics | `kubectl_basics/` | Create, inspect, debug, and access a Pod |
| Namespaces | `namespaces/` | Isolate environments and test Service DNS |

## Prerequisites

- A running Kubernetes cluster, such as Minikube
- `kubectl` configured for the cluster

## 1. Cluster Architecture

The control plane stores desired state and schedules workloads. Worker nodes run Pods through the kubelet, container runtime, and kube-proxy. Minikube usually runs these components on one node.

Useful commands:

```bash
kubectl cluster-info
kubectl get nodes -o wide
kubectl get pods -n kube-system
```

![Cluster architecture](cluster_architecture/Screenshot%202026-09-19%20at%2011.53.29%E2%80%AFPM.png)

## 2. kubectl Basics

`kubectl` communicates with the Kubernetes API server. The most useful troubleshooting commands are `get`, `describe`, and `logs`.

Apply and inspect the example Pod:

```bash
kubectl apply -f kubectl_basics/hello-pod.yaml
kubectl get pods -o wide
kubectl describe pod hello-kubectl
kubectl logs hello-kubectl
kubectl exec -it hello-kubectl -- sh
kubectl port-forward pod/hello-kubectl 8080:80
```

`kubectl apply -f` is declarative: the manifest records the desired state and can be safely applied again.

![Pod details](kubectl_basics/screenshots/Screenshot%202026-09-19%20at%2011.58.32%E2%80%AFPM.png)

![Pod logs](kubectl_basics/screenshots/Screenshot%202026-09-19%20at%2011.59.54%E2%80%AFPM.png)

![Pod shell](kubectl_basics/screenshots/Screenshot%202026-09-20%20at%2012.01.33%E2%80%AFAM.png)

![Port forwarding](kubectl_basics/screenshots/Screenshot%202026-09-20%20at%2012.03.40%E2%80%AFAM.png)

![Forwarded NGINX response](kubectl_basics/screenshots/Screenshot%202026-09-20%20at%2012.04.03%E2%80%AFAM.png)

## 3. Namespaces

Namespaces scope object names. The lab creates `yatri-dev` and `yatri-prod`; both contain a `web` Deployment and `web-service` without name conflicts.

Apply and inspect the environments:

```bash
kubectl apply -f namespaces/
kubectl get namespaces
kubectl get pods,service -n yatri-dev
kubectl get pods,service -n yatri-prod
```

Services can be reached by short names within a namespace or by their full DNS name:

```text
web-service
web-service.yatri-prod.svc.cluster.local
```

![Namespace isolation](namespaces/screenshots/Screenshot%202026-09-20%20at%205.24.02%E2%80%AFPM.png)

![Cross-namespace Service DNS](namespaces/screenshots/Screenshot%202026-09-20%20at%205.41.29%E2%80%AFPM.png)

## Takeaway

Kubernetes records desired state through the control plane, `kubectl` manages that state, and namespaces separate environments while still allowing controlled Service discovery.
