#!/bin/bash

# Define MySQL database credentials
DB_HOST="localhost"
DB_PORT="3306"
DB_USERNAME="ecommerce_user"
DB_PASSWORD="password"
DB_NAME="ecommerce_db"

# Define backup directory
BACKUP_DIR="./backups"
DATE=$(date +\%Y-\%m-\%d_\%H-\%M-\%S)
BACKUP_FILE="$BACKUP_DIR/$DB_NAME-$DATE.sql"

# Create backup directory if not exists
mkdir -p $BACKUP_DIR

# Perform MySQL backup
mysqldump -h $DB_HOST -P $DB_PORT -u $DB_USERNAME -p$DB_PASSWORD $DB_NAME > $BACKUP_FILE

echo "Backup completed: $BACKUP_FILE"
