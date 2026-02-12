📊 Event-Driven Data Processing Pipeline on AWS 🚀
📌 Project Overview

This project implements a fully automated event-driven data processing pipeline using AWS services and Infrastructure as Code (IaC) with Terraform. The pipeline captures incoming data stored in Amazon S3, processes it using AWS Lambda, and logs execution details in Amazon CloudWatch. The entire infrastructure is deployed automatically using CI/CD with GitHub Actions, without requiring local Terraform or AWS CLI setup.

🏗️ Architecture Overview

The solution uses the following AWS services:

Amazon S3 – Stores uploaded data files

AWS Lambda – Processes incoming data

Amazon EventBridge – Schedules Lambda execution (optional / extensible)

Amazon CloudWatch Logs – Stores Lambda execution logs

AWS IAM – Manages permissions securely

Terraform – Infrastructure as Code (IaC)

GitHub Actions – CI/CD automation

🔁 Workflow

Infrastructure code is pushed to the main branch.

GitHub Actions triggers the CI/CD pipeline.

Terraform provisions AWS resources automatically:

S3 bucket

IAM role

Lambda function

Data files uploaded to S3 are available for processing.

Lambda execution logs are stored in CloudWatch Logs.

⏰ Scheduling Strategy

The architecture supports scheduled execution using Amazon EventBridge (cron-based rules).
This enables batch-style processing such as daily summaries and can be extended easily without changing the core infrastructure.

🧱 Project Structure
AWS/
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Actions CI/CD pipeline
├── lambda/
│   └── lambda_function.py    # Lambda function code
├── terraform/
│   └── main.tf               # Terraform IaC configuration
└── README.md

🚀 Deployment
Automated Deployment (CI/CD – Recommended)

Push code to the main branch

GitHub Actions automatically:

Configures AWS credentials

Initializes Terraform

Applies infrastructure changes

✅ No local Terraform or AWS CLI installation required.

🔐 Security Best Practices

AWS credentials are stored securely using GitHub Secrets

IAM permissions follow least privilege principle

Root AWS account is not used

Infrastructure is managed via IaC only

📄 Infrastructure as Code (IaC)

Terraform is used to:

Create an Amazon S3 bucket

Deploy an AWS Lambda function

Assign IAM roles and policies

Enable CloudWatch logging

Package Lambda code automatically using archive_file

📈 CI/CD Implementation

CI/CD is implemented using GitHub Actions, enabling automatic deployment of cloud infrastructure on every push to the main branch. This ensures consistent, repeatable, and error-free infrastructure provisioning.

🎯 Key Outcomes

Fully automated AWS infrastructure

Event-driven, serverless architecture

Secure IAM configuration

CI/CD enabled Infrastructure as Code

Internship-ready cloud deployment

👨‍💻 Author

Ajinkya Mandlik
Cloud & DevOps Project

