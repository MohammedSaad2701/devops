# DevSecOps

This lab adds security checks to the CI/CD workflow. The goal is to catch problems early, block risky releases, and harden the running Kubernetes workload.

## Pipeline

```text
Code → Build → Test → SAST → SCA → Secret scan → Image scan → Gate → Push → Deploy
```

The pipeline checks code quality, dependency risk, leaked credentials, and image vulnerabilities before anything is pushed to production.

## What is checked

- SAST: code-level issues such as unsafe input handling
- SCA: vulnerable dependencies and package risk
- Secret scanning: API keys and tokens accidentally committed to Git
- Image scanning: vulnerabilities in the Docker image and OS packages
- Kubernetes hardening: non-root runtime, dropped capabilities, read-only filesystem, and NetworkPolicy

## Security controls

The project configures:

- `Gitleaks` for secrets detection
- `Trivy` for dependency and image scanning
- a security gate that stops the workflow when critical issues remain
- hardened pod settings in [`kubernetes/deployment.yaml`](kubernetes/deployment.yaml)
- a default-deny NetworkPolicy in [`kubernetes/networkpolicy.yaml`](kubernetes/networkpolicy.yaml)

## Screenshots

1. ![DevSecOps step 1](./screenshots/Screenshot%202026-10-11%20at%208.08.07%E2%80%AFPM.png)
2. ![DevSecOps step 2](./screenshots/Screenshot%202026-10-11%20at%208.32.28%E2%80%AFPM.png)
3. ![DevSecOps step 3](./screenshots/Screenshot%202026-10-11%20at%208.32.34%E2%80%AFPM.png)
4. ![DevSecOps step 4](./screenshots/Screenshot%202026-10-11%20at%208.35.34%E2%80%AFPM.png)
5. ![DevSecOps step 5](./screenshots/Screenshot%202026-10-11%20at%208.35.39%E2%80%AFPM.png)
6. ![DevSecOps step 6](./screenshots/Screenshot%202026-10-11%20at%208.50.22%E2%80%AFPM.png)
7. ![DevSecOps step 7](./screenshots/Screenshot%202026-10-11%20at%208.50.57%E2%80%AFPM.png)

## Summary

DevSecOps moves security left and keeps it in the delivery path. The repo shows that scanning, policy enforcement, and runtime hardening can stop bad releases before they reach Kubernetes.
