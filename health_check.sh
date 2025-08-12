#!/bin/bash
# Daily health check script

echo "Running daily health check..."
mysql -u root -ppassword -e "USE ecommerce; SOURCE sql/monitoring_queries.sql;"
echo "Health check complete."
