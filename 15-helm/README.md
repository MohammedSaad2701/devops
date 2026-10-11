# Helm Lab

This lab covers the basics of Helm, release rollback, and a small deployment project. It shows how to package Kubernetes resources, install and upgrade releases, and recover quickly when a change needs to be rolled back.

## 1. Helm commands

The first part focuses on creating a chart, rendering templates, installing a release, and checking the running state. These commands are the core of day-to-day Helm work.

```bash
helm create demo-chart
helm template demo-chart
helm install demo demo-chart
helm list
helm status demo
helm upgrade demo demo-chart
helm uninstall demo
```

![Helm commands](01-helm-commands/screenshots/Screenshot%202026-10-11%20at%206.48.02%E2%80%AFPM.png)

## 2. Rollback

If an upgrade introduces a problem, `helm rollback` restores the previous working release. This is useful when a config change or chart update breaks the app.

```bash
helm history demo
helm rollback demo 1
helm status demo
```

![Rollback](02-rollback/screenshots/Screenshot%202026-10-11%20at%207.00.16%E2%80%AFPM.png)

## 3. Mini project

The final section uses a small app chart with different values for dev and prod. The goal is to deploy the app, inspect the release, and confirm the correct configuration is used.

The chart files are in [`03-mini-project/yatri-app/`](03-mini-project/yatri-app/) and the values files are in [`03-mini-project/`](03-mini-project/).

1. ![Mini project 1](03-mini-project/screenshots/Screenshot%202026-10-11%20at%206.55.57%E2%80%AFPM.png)
2. ![Mini project 2](03-mini-project/screenshots/Screenshot%202026-10-11%20at%206.57.41%E2%80%AFPM.png)
3. ![Mini project 3](03-mini-project/screenshots/Screenshot%202026-10-11%20at%206.58.11%E2%80%AFPM.png)
4. ![Mini project 4](03-mini-project/screenshots/Screenshot%202026-10-11%20at%206.58.30%E2%80%AFPM.png)
5. ![Mini project 5](03-mini-project/screenshots/Screenshot%202026-10-11%20at%206.58.37%E2%80%AFPM.png)
6. ![Mini project 6](03-mini-project/screenshots/Screenshot%202026-10-11%20at%206.58.52%E2%80%AFPM.png)
7. ![Mini project 7](03-mini-project/screenshots/Screenshot%202026-10-11%20at%206.59.40%E2%80%AFPM.png)
8. ![Mini project 8](03-mini-project/screenshots/Screenshot%202026-10-11%20at%207.01.16%E2%80%AFPM.png)
9. ![Mini project 9](03-mini-project/screenshots/Screenshot%202026-10-11%20at%207.01.23%E2%80%AFPM.png)

## Summary

Helm helps make Kubernetes deployments consistent, repeatable, and easier to manage. The main ideas from this lab are: create a chart, install and upgrade releases, use values for environment differences, and rollback quickly when needed.
