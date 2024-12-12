#!/bin/bash

# Define MySQL database credentials
DB_HOST="localhost"
DB_PORT="3306"
DB_USERNAME="ecommerce_user"
DB_PASSWORD="password"
DB_NAME="ecommerce_db"

# Define the CSV file to import
CSV_FILE="./data/sales_data.csv"

# Refresh the sales data by importing the CSV file
mysqlimport --local --ignore-lines=1 --fields-terminated-by=',' --columns='product_id,quantity,sale_date' -u $DB_USERNAME -p$DB_PASSWORD -h $DB_HOST -P $DB_PORT $DB_NAME $CSV_FILE

echo "Sales data refresh completed."
