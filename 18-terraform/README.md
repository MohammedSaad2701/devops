# Terraform practice repo

This folder contains Terraform exercises for AWS services and a demo infrastructure project.

## Contents

- `aws-services/` — service-focused Terraform exercises
- `terraform-demo/` — an example AWS stack using a VPC, subnet, EC2, IAM, and S3
- `screenshots/` — captured results from the LocalStack-based S3 Terraform demo

## Short summary of the S3 demo

This exercise demonstrates how to provision a secure S3 bucket with Terraform in a local AWS-compatible environment using LocalStack.

The workflow starts by pointing the AWS provider to LocalStack and validating that the core AWS services are available. After `terraform init`, `terraform fmt`, and `terraform validate`, the project creates a bucket with a random suffix, enables versioning, applies server-side encryption, blocks public access, enforces bucket ownership, and rejects insecure HTTP traffic through a TLS-only bucket policy.

Once the plan is approved, Terraform creates the bucket and uploads a sample object such as `hello.txt`. The result is a simple but realistic example of how a production-ready S3 setup can be defined as infrastructure as code, while still being safe and easy to test locally.

## Screenshot log

### LocalStack health check and provider setup

![LocalStack health check](./screenshots/Screenshot%202026-10-11%20at%2010.03.46%E2%80%AFPM.png)

### Terraform init and validation

![Terraform init and validation](./screenshots/Screenshot%202026-10-11%20at%2010.09.25%E2%80%AFPM.png)

### Terraform plan preview

![Terraform plan preview](./screenshots/Screenshot%202026-10-11%20at%2010.09.32%E2%80%AFPM.png)

### Bucket creation and object upload result

![Bucket creation result](./screenshots/Screenshot%202026-10-11%20at%2010.09.50%E2%80%AFPM.png)

## Notes

- Review the AWS documentation and costs before applying changes in a real environment.
- Use LocalStack for safe, low-cost testing when validating Terraform patterns.
- The service-specific guides in `aws-services/` provide more detail on IAM, EC2, S3, VPC, and DynamoDB/RDS.
