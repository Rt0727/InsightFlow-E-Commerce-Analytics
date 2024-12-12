provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ecommerce_ec2" {
  ami           = "ami-12345678"  # Replace with the latest AMI
  instance_type = "t2.micro"
  key_name      = var.key_name
  tags = {
    Name = "ecommerce-instance"
  }
}

resource "aws_security_group" "ecommerce_sg" {
  name_prefix = "ecommerce-sg"
  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_db_instance" "ecommerce_db" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t2.micro"
  db_name              = var.db_name
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
  publicly_accessible  = true
}
