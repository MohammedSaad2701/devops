# Observability

Observability is the ability to understand a running system from the signals it emits. It goes beyond simple dashboards and alerts: it helps answer what is happening, why it happened, and where the problem is.

## Monitoring vs observability

Monitoring tells you when something is wrong: CPU is high, a pod is unhealthy, or the error rate jumped.

Observability explains why: which dependency slowed the request, which pod failed, or which change introduced the issue.

A simple way to think about it:

- Monitoring: detect a problem
- Observability: understand the problem

## The three pillars

### Metrics

Metrics are numeric signals over time: CPU, memory, request rate, latency, and errors.

Common patterns include:
- RED: rate, errors, duration
- USE: utilisation, saturation, errors
- SRE golden signals: latency, traffic, errors, saturation

Prometheus is the standard tool for collecting and querying metrics.

### Logs

Logs record discrete events and are useful for debugging. They are detailed but noisy, so structured logs are preferred over plain text.

Best practice:
- use structured JSON
- include request IDs or trace IDs
- avoid logging secrets or personal data

### Traces

Traces follow one request through the system. They show where time was spent and which service introduced the delay.

## Why they matter together

A healthy system needs all three signals:

```text
Alert fires -> metric shows the spike
Trace identifies the slow step
Logs explain the exact failure or dependency issue
```

When metrics, logs, and traces are connected by labels such as service, namespace, pod, and trace ID, they become real observability rather than disconnected data sources.

## Kubernetes observability

In Kubernetes, useful signals include:

- pod health and readiness
- deployment replica status
- node CPU and memory usage
- container limits and throttling
- app-level RED metrics
- cluster events and crashes

Useful commands:

```bash
kubectl top nodes
kubectl top pods -A
kubectl get events -A --sort-by=.lastTimestamp
kubectl describe pod <pod>
kubectl logs <pod> --previous
```

## Common stack

A common open-source setup is:

- Prometheus for metrics
- Alertmanager for alert routing
- Grafana for dashboards
- Loki for logs
- Tempo or Jaeger for traces

This project applies those ideas in practice with a live monitoring demo on minikube.
