# Cloud & Terraform in Action

This project shows a complete Terraform workflow for a small AWS-style web workload running locally against LocalStack.

The configuration in `terraform/` provisions:

- a VPC and public subnet
- an Internet Gateway and route table
- an EC2 web instance
- IAM role and instance profile
- an S3 bucket for website content
- security groups and TLS-only bucket protection

The setup is designed to model a realistic cloud deployment while keeping the environment safe and easy to test locally.

## What this workflow demonstrates

- `terraform init` downloads the required providers
- `terraform fmt` and `terraform validate` verify formatting and configuration correctness
- `terraform graph` shows the dependency relationships between resources
- `terraform plan` previews the infrastructure that will be created
- `terraform apply` creates the full stack in LocalStack

## Summary of the Terraform setup

The project creates a VPC with a public subnet and an EC2 instance running Amazon Linux 2023. The instance is assigned an IAM role that allows read-only access to an S3 bucket containing the site assets. The bucket is protected by public access blocking, encryption, and a policy that denies insecure HTTP transport.

This is a good example of AWS best practices in Terraform:

- least-privilege IAM permissions
- private bucket protections
- TLS enforcement
- encrypted storage
- explicit dependency wiring between EC2, IAM, networking, and S3 resources

## Evidence log

### Terraform init and provider setup

```text
$ terraform init
Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/random from the dependency lock file
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using hashicorp/random v3.9.1 from the shared cache directory
- Using hashicorp/aws v5.100.0 from the shared cache directory

Terraform has been successfully initialized!
```

### Terraform validation

```text
$ terraform fmt -recursive
$ terraform fmt -check
$ terraform validate
Success! The configuration is valid.
```

### Dependency graph

```text
$ terraform graph | grep -E '"(aws_|random_)[^"]*" -> "(aws_|random_)' | sed -E 's/\[root\] //g; s/ \(expand\)//g' | sort
  "aws_iam_instance_profile.web" -> "aws_iam_role.web";
  "aws_iam_role_policy.read_assets" -> "aws_iam_role.web";
  "aws_iam_role_policy_attachment.ssm" -> "aws_iam_role.web";
  "aws_instance.web" -> "aws_iam_instance_profile.web";
  "aws_instance.web" -> "aws_s3_object.index";
  "aws_internet_gateway.igw" -> "aws_vpc.main";
  "aws_s3_bucket.assets" -> "random_id.bucket_suffix";
  "aws_security_group.web" -> "aws_vpc.main";
  "aws_subnet.public" -> "aws_vpc.main";
```

### Terraform plan highlights

```text
Terraform will perform the following actions:
  # aws_iam_role.web will be created
  # aws_iam_instance_profile.web will be created
  # aws_instance.web will be created
  # aws_security_group.web will be created
  # aws_subnet.public will be created
  # aws_internet_gateway.igw will be created
  # aws_route_table.public will be created
  # aws_s3_bucket.assets will be created
  # aws_s3_object.index will be created
```

## Screenshots

### LocalStack and provider health

![LocalStack and provider health](./screenshots/Screenshot%202026-10-11%20at%2010.15.58%E2%80%AFPM.png)

### Terraform init output

![Terraform init output](./screenshots/Screenshot%202026-10-11%20at%2010.16.53%E2%80%AFPM.png)

### Terraform plan details

![Terraform plan details](./screenshots/Screenshot%202026-10-11%20at%2010.17.14%E2%80%AFPM.png)

### Final deployment and infrastructure state

![Final deployment and infrastructure state](./screenshots/Screenshot%202026-10-11%20at%2010.17.48%E2%80%AFPM.png)

## Notes

- Review the generated plan before applying changes to any real AWS account.
- LocalStack is useful for validating Terraform patterns without cloud cost or risk.
- Destroy the resources after testing to keep the environment clean.
- For more AWS service explanations, see the related exercises in the surrounding Terraform learning folders.
