📊 Event-Driven Data Processing Pipeline on AWS
📌 Project Overview

This project implements a fully automated event-driven data processing pipeline using AWS services and Infrastructure as Code (IaC) with Terraform.
The pipeline captures incoming data, stores it in Amazon S3, processes it using AWS Lambda, and generates automated daily summary reports triggered via Amazon EventBridge.
Continuous Integration and Deployment (CI/CD) is implemented using GitHub Actions.

🏗️ Architecture Overview

The solution uses the following AWS services:

Amazon S3 – Stores uploaded data files

AWS Lambda – Processes data and generates summaries

Amazon EventBridge – Triggers Lambda on a daily schedule

Amazon CloudWatch Logs – Stores Lambda execution logs

AWS IAM – Manages permissions securely

GitHub Actions – Automates deployment (CI/CD)

Terraform – Infrastructure as Code (IaC)

🔁 Workflow

Data files are uploaded to Amazon S3.

Amazon EventBridge triggers the Lambda function once daily at a fixed time.

AWS Lambda reads data from S3 and processes it.

Processed results and execution logs are stored in CloudWatch Logs.

Infrastructure changes are automatically deployed using GitHub Actions.

⏰ Scheduling Strategy

The Lambda function is triggered once per day using a cron-based EventBridge rule.

This batch-processing approach is cost-effective and suitable for generating daily summary reports.

🧱 Project Structure
AWS/
│
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Actions CI/CD pipeline
│
├── lambda/
│   └── lambda_function.py    # Lambda function code
│
├── terraform/
│   └── main.tf               # Terraform IaC configuration
│
└── README.md

🚀 Deployment Steps
Prerequisites

AWS Account (Free Tier)

IAM User with programmatic access

AWS CLI configured (aws configure)

Terraform installed

GitHub account

Local Deployment (Manual)
terraform init
terraform apply

Automated Deployment (CI/CD)

Push changes to the main branch

GitHub Actions automatically:

Configures AWS credentials

Initializes Terraform

Applies infrastructure changes

🔐 Security Best Practices

AWS credentials are stored securely using GitHub Secrets

IAM access is limited to required permissions

Terraform state files are excluded using .gitignore

Root AWS account is not used for development

📄 Infrastructure as Code (IaC)

Terraform is used to:

Create S3 bucket

Deploy Lambda function

Configure EventBridge schedule

Assign IAM roles and policies

Enable CloudWatch logging

📈 CI/CD Implementation

CI/CD is implemented using GitHub Actions, enabling automated deployment of infrastructure on every push to the main branch.

🎯 Key Outcomes

Fully automated cloud infrastructure

Event-driven and scheduled processing

Secure and scalable design

CI/CD enabled deployment pipeline

👨‍💻 Author

Ajinkya Mandlik
Internship Project – Cloud & DevOps
