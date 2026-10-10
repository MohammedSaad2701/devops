# Kubernetes Troubleshooting Commands

This guide demonstrates common `kubectl` commands using a two-replica NGINX Deployment in the `ts-cmds` namespace. The manifest is in [`01-commands/ts-cmds-deployment.yaml`](01-commands/ts-cmds-deployment.yaml); command output screenshots are included below in numbered order.

## Quick command guide

| To find out... | Use |
| --- | --- |
| What resources exist and their status | `kubectl get` |
| Which node and IP a Pod uses | `kubectl get -o wide` |
| Why a resource is stuck | `kubectl describe` and check Events |
| What a container logged | `kubectl logs` |
| What the container sees internally | `kubectl exec` |
| What happened over time | `kubectl events` |
| How an API field works | `kubectl explain` |
| Current CPU and memory use | `kubectl top` |

Start with **get → describe → logs → exec**. Check events and resource usage if the issue remains unclear.

## Inspect resources

```sh
kubectl get all -n ts-cmds
kubectl get pods -n ts-cmds --show-labels
kubectl get pods -n ts-cmds -o wide
kubectl get pods -A --field-selector=status.phase!=Running
kubectl get pod <pod> -n ts-cmds -o yaml
kubectl describe pod <pod> -n ts-cmds
kubectl describe service web -n ts-cmds
```

Use `-o wide` to see Pod IPs and node placement. `describe` includes status, conditions, and recent events that can explain a failure.

## Check logs and containers

```sh
kubectl logs <pod> -n ts-cmds --tail=20
kubectl logs -l app=web -n ts-cmds --tail=5 --prefix
kubectl logs <pod> -n ts-cmds --previous
kubectl exec <pod> -n ts-cmds -- nginx -v
kubectl exec <pod> -n ts-cmds -- cat /etc/resolv.conf
kubectl exec <pod> -n ts-cmds -- sh -c 'ps; df -h /'
```

Use `--previous` to inspect the last terminated container instance. To test Service DNS, run a client Pod in the namespace and use `kubectl exec` from it.

## Events, API reference, and metrics

```sh
kubectl events -n ts-cmds
kubectl events -n ts-cmds --for pod/<pod>
kubectl events -A --types=Warning
kubectl explain pod.spec.containers.readinessProbe
kubectl top nodes
kubectl top pods -n ts-cmds --containers
```

Events are temporary, so collect them soon after a problem occurs. `kubectl top` requires metrics-server; on Minikube, enable it with `minikube addons enable metrics-server`. Newly started workloads may take a short time to appear in metrics.

## Other useful checks

```sh
kubectl auth can-i list secrets -n ts-cmds
kubectl api-resources --namespaced=true -o name
kubectl cluster-info
kubectl get --raw='/readyz?verbose'
kubectl get deployment web -n ts-cmds -o yaml
```

## Screenshots

The following images are from [`01-commands/screenshots/`](01-commands/screenshots/) and are listed in filename order.

1. ![Screenshot 1](01-commands/screenshots/1.png)
2. ![Screenshot 2](01-commands/screenshots/2.png)
3. ![Screenshot 3](01-commands/screenshots/3.png)
4. ![Screenshot 4](01-commands/screenshots/4.png)
5. ![Screenshot 5](01-commands/screenshots/5.png)
6. ![Screenshot 6](01-commands/screenshots/6.png)
7. ![Screenshot 7](01-commands/screenshots/7.png)
8. ![Screenshot 8](01-commands/screenshots/8.png)
9. ![Screenshot 9](01-commands/screenshots/9.png)
10. ![Screenshot 10](01-commands/screenshots/10.png)
11. ![Screenshot 11](01-commands/screenshots/11.png)
12. ![Screenshot 12](01-commands/screenshots/12.png)
13. ![Screenshot 13](01-commands/screenshots/13.png)
14. ![Screenshot 14](01-commands/screenshots/14.png)
15. ![Screenshot 15](01-commands/screenshots/15.png)
16. ![Screenshot 16](01-commands/screenshots/16.png)
17. ![Screenshot 17](01-commands/screenshots/17.png)
18. ![Screenshot 18](01-commands/screenshots/18.png)
19. ![Screenshot 19](01-commands/screenshots/19.png)
20. ![Screenshot 20](01-commands/screenshots/20.png)
21. ![Screenshot 21](01-commands/screenshots/21.png)
22. ![Screenshot 22](01-commands/screenshots/22.png)
23. ![Screenshot 23](01-commands/screenshots/23.png)

## Common Kubernetes Issues

These examples reproduce nine frequent Kubernetes failures with broken manifests, then resolve them with corrected configurations. Follow the same workflow for each: **identify → investigate → fix → verify**. Manifests are in [`02-common-issues/`](02-common-issues/).

| Issue | Common signal | Typical cause |
| --- | --- | --- |
| [CrashLoopBackOff](02-common-issues/01-crashloopbackoff/) | Restart count rises; `BackOff` events | The process exits, often due to missing configuration |
| [ImagePullBackOff](02-common-issues/02-imagepullbackoff/) | `ImagePullBackOff` | Invalid image tag or registry access |
| [ErrImagePull](02-common-issues/03-errimagepull/) | `ErrImagePull` | Invalid or private image repository |
| [Pending](02-common-issues/04-pending/) | No node assignment or Pod IP | Requests exceed capacity or node selector matches no node |
| [ContainerCreating](02-common-issues/05-containercreating/) | Pod stays in `ContainerCreating` | Required Secret or volume is missing |
| [Service connectivity](02-common-issues/06-service-connectivity/) | Service request fails | Selector matches no Pods or `targetPort` is wrong |
| [DNS](02-common-issues/07-dns-issues/) | `NXDOMAIN` | Incorrect Service name or namespace |
| [Pod networking](02-common-issues/08-pod-networking/) | Connection refused at the Pod IP | Application listens only on `127.0.0.1` |
| [Configuration](02-common-issues/09-configuration/) | `CreateContainerConfigError` | Missing ConfigMap, wrong key, or invalid command |

### 1. CrashLoopBackOff

Check the restart count, previous logs, and Pod events:

```sh
kubectl get pods
kubectl logs <pod> --previous
kubectl describe pod <pod>
```

In this example, the process exited because `/etc/app/config.yaml` was missing. Mount a ConfigMap with the required file, then confirm the replacement Pod is running without restarts.

### 2. ImagePullBackOff

Use `kubectl describe pod <pod>` and inspect Events for the failed image reference. In this example the repository exists, but the tag does not. Correct the image name or tag.

### 3. ErrImagePull

An invalid or private repository can prevent access. Correct the repository reference, or configure an image-pull Secret if the image is private.

### 4. Pending Pods

```sh
kubectl get pods -o wide
kubectl describe pod <pod>
kubectl describe node <node>
```

`FailedScheduling` events identify resource shortages or node-selector mismatches. Reduce unrealistic CPU or memory requests, or ensure a matching node label exists.

### 5. ContainerCreating

Inspect Pod events for mount and volume errors. The example references a Secret that has not been created; create the required Secret and Kubernetes can retry the mount without recreating the Pod.

### 6. Service connectivity

Compare Service selectors with Pod labels, then check the endpoints:

```sh
kubectl get svc <service> -o yaml
kubectl get pods --show-labels
kubectl get endpointslices -l kubernetes.io/service-name=<service>
```

No endpoints usually means the selector does not match. If endpoints exist but requests are refused, verify that `targetPort` matches the port where the application listens.

### 7. DNS

Check the client Pod's `/etc/resolv.conf` and use the Service's namespace-qualified DNS name when crossing namespaces, for example:

```text
backend.backend-ns.svc.cluster.local
```

Confirm the Service exists and CoreDNS is healthy before changing DNS configuration.

### 8. Pod networking

If a server works inside its Pod but cannot be reached at the Pod IP, inspect its listening address:

```sh
kubectl exec <pod> -- netstat -tln
```

Binding to `127.0.0.1` limits access to the Pod itself. Bind to `0.0.0.0` or the appropriate interface instead. Also verify readiness probes and whether the cluster's CNI enforces NetworkPolicies.

### 9. Configuration errors

Kubernetes may report configuration problems one at a time. Check referenced ConfigMaps, required keys, mounted files, and the container command; correct each issue, then wait for the Pod to become ready.

## Common-issue screenshots

Screenshots from [`02-common-issues/screenshots/`](02-common-issues/screenshots/) are shown in filename order:

1. `1_1.png`
   ![Common issue screenshot 1_1](02-common-issues/screenshots/1_1.png)
2. `1_2.png`
   ![Common issue screenshot 1_2](02-common-issues/screenshots/1_2.png)
3. `2_1.png`
   ![Common issue screenshot 2_1](02-common-issues/screenshots/2_1.png)
4. `2_2.png`
   ![Common issue screenshot 2_2](02-common-issues/screenshots/2_2.png)
5. `3_1.png`
   ![Common issue screenshot 3_1](02-common-issues/screenshots/3_1.png)
6. `3_2.png`
   ![Common issue screenshot 3_2](02-common-issues/screenshots/3_2.png)
7. `4_1.png`
   ![Common issue screenshot 4_1](02-common-issues/screenshots/4_1.png)
8. `4_2.png`
   ![Common issue screenshot 4_2](02-common-issues/screenshots/4_2.png)
9. `4_3.png`
   ![Common issue screenshot 4_3](02-common-issues/screenshots/4_3.png)
10. `4_4.png`
    ![Common issue screenshot 4_4](02-common-issues/screenshots/4_4.png)
11. `4_5.png`
    ![Common issue screenshot 4_5](02-common-issues/screenshots/4_5.png)
12. `5_1.png`
    ![Common issue screenshot 5_1](02-common-issues/screenshots/5_1.png)
13. `5_2.png`
    ![Common issue screenshot 5_2](02-common-issues/screenshots/5_2.png)
14. `6_1.png`
    ![Common issue screenshot 6_1](02-common-issues/screenshots/6_1.png)
15. `7_1.png`
    ![Common issue screenshot 7_1](02-common-issues/screenshots/7_1.png)
16. `8_1.png`
    ![Common issue screenshot 8_1](02-common-issues/screenshots/8_1.png)
17. `8_2.png`
    ![Common issue screenshot 8_2](02-common-issues/screenshots/8_2.png)
18. `9_1.png`
    ![Common issue screenshot 9_1](02-common-issues/screenshots/9_1.png)
19. `9_2.png`
    ![Common issue screenshot 9_2](02-common-issues/screenshots/9_2.png)