variable "aws_region" {
  default = "ap-south-1"
}

variable "cluster_name" {
  default = "taskboard-eks"
}

variable "environment" {
  default = "dev"
}

variable "cluster_version" {
  description = "Kubernetes version for the EKS cluster"
  type        = string
  default     = "1.33"
}
