# InsightFlow: E-Commerce Analytics

## Overview
This repository provides an automated setup for an e-commerce analytics dashboard powered by MySQL, Terraform, and Docker. It features a seamless integration between a MySQL database and a Flask web application to offer insightful analytics for e-commerce sales. The setup uses Terraform for Infrastructure as Code (IaC) to manage cloud resources and Docker for containerizing the application.

## Features
- **MySQL Database**: Stores sales, product, and customer data.
- **Flask Web Application**: Provides an analytics dashboard for real-time insights into e-commerce metrics.
- **Infrastructure as Code**: Automates the setup of EC2 instances and RDS MySQL databases using Terraform.
- **Data Refresh**: Includes a script to regularly refresh e-commerce data for accurate reporting.
- **Backup Automation**: Automated script to back up MySQL databases for disaster recovery.
- **Containerized Environment**: Docker ensures consistent environments for both development and production setups.

## 🛠️ Technologies Used

| Technology        | Purpose                               |
|-------------------|---------------------------------------|
| **PostgreSQL**    | Database for library data            |
| **Docker**        | Containerization                     |
| **Terraform**     | Infrastructure provisioning          |
| **Bash Scripts**  | Automation of routine tasks          |
| **Python**        | Core application logic for the CLI   |

## Prerequisites
- Install [Docker](https://www.docker.com/)
- Install [Terraform](https://www.terraform.io/)
- Install [Git](https://git-scm.com/)
- Basic knowledge of Bash and Python
- AWS Account for deploying infrastructure (Optional, if using AWS EC2/RDS)

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine and navigate into the directory:
```bash
git clone https://github.com/yourusername/ecommerce-analytics-dashboard-setup.git
cd ecommerce-analytics-dashboard-setup
```

### 2. Configure Terraform Variables
Create a `.tfvars` file in the `terraform/` directory with the following contents:
```hcl
ec2_instance_type  = "t2.micro"
rds_db_instance_class = "db.t2.micro"
db_name            = "ecommerce_db"
db_username        = "admin"
db_password        = "password"
aws_region         = "us-east-1"
```

### 3. Initialize and Deploy Infrastructure
Use Terraform to initialize and deploy the necessary infrastructure:
```bash
cd terraform
terraform init
terraform apply -var-file="variables.tfvars"
```
This will set up an EC2 instance for the web app and an RDS MySQL instance for the database. The Terraform output will include the RDS MySQL endpoint.

### 4. Build and Start Docker Containers
Navigate back to the root directory and build the Docker containers:
```bash
docker-compose up --build
```
This will:
- Build the Docker image for the Flask web application.
- Start the MySQL database and Flask application containers.

### 5. Access the Analytics Dashboard
To interact with the e-commerce analytics dashboard, access the Flask app:
```bash
docker-compose exec app flask run
```
The dashboard will be accessible at `http://localhost:5000`.

### 6. Use Backup and Data Refresh Scripts
Automate database backups and data refresh with the provided scripts:

#### Run Backup Script
```bash
./scripts/backup.sh
```
This script creates a backup of the MySQL database to ensure data safety.

#### Refresh Sales Data
```bash
./scripts/data_refresh.sh
```
This script refreshes the sales data in the MySQL database for up-to-date insights.

## Project Structure
```plaintext
ecommerce-analytics-dashboard-setup/
│
├── terraform/
│   ├── main.tf                    # Defines EC2 and RDS MySQL resources
│   ├── variables.tf               # Contains variables for EC2, RDS setup
│   └── outputs.tf                 # Outputs RDS endpoint and EC2 instance details
│
├── docker/
│   ├── Dockerfile                 # Dockerfile for Flask web app
│   └── docker-compose.yml         # Docker Compose file for local setup
│
├── scripts/
│   ├── backup.sh                  # Backup script for MySQL database
│   └── data_refresh.sh            # Sales data refresh script
│
├── README.md                      # Documentation
└── .gitignore                     # Git ignore file
```

## Troubleshooting

### Common Issues
1. **Terraform Errors**: Ensure that Terraform is installed and the `variables.tfvars` file is correctly configured.
2. **Docker Issues**: Verify that Docker is running and the containers are built correctly.
3. **Database Connection Errors**: Check that the MySQL container is running and matches the configuration in `variables.tfvars`.

### Logs
Access logs for debugging:
- Flask App Logs: Run `docker-compose logs app`
- MySQL Logs: Run `docker-compose logs db`

## Future Enhancements
- Implement advanced analytics features (e.g., sales forecasts, trend analysis).
- Add role-based access control to the dashboard for secure user management.
- Integrate external data sources for a more comprehensive analytics experience.

---

For any questions or issues, feel free to reach out at `rt07mahifan@gmail.com`.

--- 

