# Observability

Observability is the ability to understand a system from the signals it emits. It is broader than dashboards and basic alerting: it lets you answer questions you did not know to ask in advance.

## Monitoring vs observability

**Monitoring** tells you when something is likely wrong: CPU is high, the error rate jumped, or a service is down.

**Observability** helps you explain why: which dependency slowed the request, which pod failed, or which version introduced the issue.

| Area | Monitoring | Observability |
| --- | --- | --- |
| Questions | Known in advance | Unclear at the start |
| Output | Alerts and dashboards | Correlated metrics, logs and traces |
| Goal | Detect issues | Understand root cause |

Monitoring is a subset of observability, not a replacement for it.

## The three pillars

### 1. Metrics

Metrics are numeric time-series data: CPU, request rate, latency, queue depth, error count.

Common patterns:
- RED: rate, errors, duration
- USE: utilisation, saturation, errors
- SRE golden signals: latency, traffic, errors, saturation

Prometheus is the standard choice for collecting and querying metrics.

### 2. Logs

Logs are timestamped records of discrete events. They are rich in detail but noisy and expensive at scale.

Best practice:
- use structured JSON logs
- include a `trace_id` or request ID
- avoid logging secrets and personal data

### 3. Traces

Traces show the full path of one request across services. They answer: where did the time go, and which service caused the delay?

A trace is made of spans. Each span records one unit of work, its duration, and metadata.

## Why they matter together

A healthy system needs all three:

```text
Metric alert fires: p99 latency is high
        ↓
Trace shows the slow step
        ↓
Logs show the error detail and dependency response
```

When metrics, logs and traces are correlated by labels like `service`, `namespace`, `pod`, and `trace_id`, they become true observability instead of three disconnected signals.

## Why observability is important

- Distributed systems fail in ways teams do not predict ahead of time
- Kubernetes Pods are short-lived and move around
- Outages are often caused by slow diagnosis, not just bad code
- SLOs and error budgets require meaningful measurements
- Deployments and rollbacks need evidence from live systems

## Common tools

| Category | Typical tools |
| --- | --- |
| Metrics | Prometheus, Mimir, Thanos, VictoriaMetrics |
| Logs | Loki, Elasticsearch/OpenSearch, Fluent Bit, Vector |
| Traces | Jaeger, Tempo, Zipkin |
| Visualisation | Grafana, Kibana |
| Alerting | Alertmanager, Grafana Alerting |
| Instrumentation | OpenTelemetry |

OpenTelemetry is the standard way to emit metrics, logs and traces from applications. It keeps instrumentation vendor-neutral so data can be sent to different backends later.

A typical open-source stack is often called LGTM:

```text
Apps (OTel SDK) → OpenTelemetry Collector → Prometheus / Loki / Tempo → Grafana
                                                    ↘ Alertmanager → Slack / PagerDuty
```

## Kubernetes observability

Kubernetes adds another layer of signals to track:

| Layer | What to watch |
| --- | --- |
| Cluster / control plane | API server health, scheduler, etcd |
| Nodes | CPU, memory, disk, pressure |
| Kubernetes objects | Replica counts, Pod state, restarts, HPA |
| Containers | usage vs requests/limits, throttling, OOM |
| Applications | RED metrics, business metrics |
| Logs | all container stdout/stderr |
| Events | scheduling, image pull, readiness failures |

Useful commands:

```bash
kubectl top nodes
kubectl top pods -A
kubectl get events -A --sort-by=.lastTimestamp
kubectl describe pod <pod>
kubectl logs <pod> --previous
```

For production-style monitoring, the kube-prometheus-stack is a common starting point because it includes Prometheus, Alertmanager, Grafana, node-exporter and kube-state-metrics.

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace
```

## Core alerts to start with

- Pod crash looping
- Pod not ready
- Deployment replicas unavailable
- Container near memory limit
- CPU throttling
- Node not ready
- PVC nearly full
- High error rate

The [monitoring demo](../01-monitoring/) in this session applies these ideas in practice with Prometheus, Grafana, Alertmanager and an instrumented app on minikube.
