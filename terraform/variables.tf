variable "key_name" {
  description = "The name of the EC2 key pair"
  type        = string
}

variable "db_name" {
  description = "The name of the MySQL database"
  type        = string
}

variable "db_username" {
  description = "The username for MySQL database"
  type        = string
}

variable "db_password" {
  description = "The password for MySQL database"
  type        = string
}
