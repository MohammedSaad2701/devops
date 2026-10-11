# CI/CD

This project shows a simple GitHub Actions workflow for a Node.js API. It validates the code, builds a container image, and deploys the app to Kubernetes.

## Contents

- `app/` — application source and tests
- `kubernetes/` — deployment and service manifests
- `screenshots/` — project evidence screenshots

Run checks from `app/` with `npm test` and `npm run lint`.

## CI vs CD

CI and CD are related but answer different questions.

| Stage | Main question | Typical trigger | Main outcome |
| --- | --- | --- | --- |
| CI | Does this change still work? | Every push or pull request | Build, lint, and test results |
| Delivery | Is this build ready to release? | Merge to main | A verified artifact for release |
| Deployment | Release it to production | Approved deploy path | App goes live |

CI focuses on correctness. It runs fast checks such as install, lint, unit tests, and container build validation. CD turns a successful build into a routine, repeatable release process. Delivery usually waits for approval, while Deployment can happen automatically once the workflow is approved.

In this project, the deployment workflow targets the `production` GitHub environment. That means the release is still automated, but GitHub can require a reviewer before the final deployment proceeds. In practice, this behaves like continuous delivery with an approval gate.

## Workflow screenshots

1. ![CI/CD screenshot 1](./screenshots/Screenshot%202026-10-11%20at%207.06.56%E2%80%AFPM.png)
2. ![CI/CD screenshot 2](./screenshots/Screenshot%202026-10-11%20at%207.14.16%E2%80%AFPM.png)
3. ![CI/CD screenshot 3](./screenshots/Screenshot%202026-10-11%20at%207.15.02%E2%80%AFPM.png)
4. ![CI/CD screenshot 4](./screenshots/Screenshot%202026-10-11%20at%207.15.22%E2%80%AFPM.png)
5. ![CI/CD screenshot 5](./screenshots/Screenshot%202026-10-11%20at%207.16.17%E2%80%AFPM.png)
6. ![CI/CD screenshot 6](./screenshots/Screenshot%202026-10-11%20at%207.16.51%E2%80%AFPM.png)
7. ![CI/CD screenshot 7](./screenshots/Screenshot%202026-10-11%20at%207.17.15%E2%80%AFPM.png)
8. ![CI/CD screenshot 8](./screenshots/Screenshot%202026-10-11%20at%207.17.41%E2%80%AFPM.png)
9. ![CI/CD screenshot 9](./screenshots/Screenshot%202026-10-11%20at%207.18.03%E2%80%AFPM.png)
10. ![CI/CD screenshot 10](./screenshots/Screenshot%202026-10-11%20at%207.18.13%E2%80%AFPM.png)

## Summary

The workflow keeps the main branch healthy through automated checks and makes release steps repeatable. A working CI pipeline lowers risk, and a controlled CD process helps teams ship faster without losing oversight.
