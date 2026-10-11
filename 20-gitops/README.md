# GitOps and monitoring lab

This project combines Kubernetes monitoring with GitOps in a compact lab. It shows how telemetry, alerting, and Git-driven deployment work together in a real cluster.

## What this lab shows

- Prometheus collecting metrics from the app and Kubernetes
- Grafana dashboards for health, traffic, and resource usage
- Alertmanager routing active and resolved alerts
- Argo CD syncing the cluster state from Git
- self-healing, rollback, and prune behavior from repository changes

## Quick setup

```bash
minikube image load metrics-app:1.0.0
kubectl apply -f 01-monitoring/k8s/00-namespace.yaml
kubectl -n monitoring create secret generic grafana-admin --from-literal=password=admin123
kubectl apply -f 01-monitoring/k8s/
kubectl -n monitoring port-forward svc/grafana 3000:3000
kubectl -n monitoring port-forward svc/prometheus 9090:9090
```

## Short summary

An instrumented app generated normal traffic, CPU-heavy `/work` requests, and failing `/error` requests. Prometheus gathered the metrics, kube-state-metrics and cAdvisor exposed resource usage, and Grafana visualised the results. In the GitOps flow, Argo CD watched the Git repository, applied the desired state to the cluster, and corrected drift automatically. The demo also showed a bad commit being rejected, a revert restoring the last working state, and a deleted object being pruned when the Git source changed.

## Screenshot evidence

### Grafana dashboard

![Grafana metrics dashboard](./screenshots/Screenshot%202026-10-11%20at%2010.22.50%E2%80%AFPM.png)

### Prometheus targets

![Prometheus targets](./screenshots/Screenshot%202026-10-11%20at%2010.24.42%E2%80%AFPM.png)

### Prometheus alerts

![Prometheus alerts](./screenshots/Screenshot%202026-10-11%20at%2010.34.40%E2%80%AFPM.png)

### Alertmanager alerts

![Alertmanager alerts](./screenshots/Screenshot%202026-10-11%20at%2010.34.46%E2%80%AFPM.png)

### Request rate by route and status

![Request rate by route and status](./screenshots/Screenshot%202026-10-11%20at%2010.36.02%E2%80%AFPM.png)

### Monitoring setup

![Monitoring setup](./screenshots/Screenshot%202026-10-11%20at%2010.37.29%E2%80%AFPM.png)

### Observability view

![Observability view](./screenshots/Screenshot%202026-10-11%20at%2010.38.00%E2%80%AFPM.png)

### Cluster status

![Cluster status](./screenshots/Screenshot%202026-10-11%20at%2010.38.49%E2%80%AFPM.png)

### GitOps flow

![GitOps flow](./screenshots/Screenshot%202026-10-11%20at%2010.46.07%E2%80%AFPM.png)

### GitOps deployment status

![GitOps deployment status](./screenshots/Screenshot%202026-10-11%20at%2010.39.42%E2%80%AFPM.png)

### GitOps sync and drift recovery

![GitOps sync and drift recovery](./screenshots/Screenshot%202026-10-11%20at%2010.49.20%E2%80%AFPM.png)

## Main takeaway

The main lesson is that observability and GitOps work best together: telemetry shows what is happening, while Git remains the source of truth for the cluster state.
