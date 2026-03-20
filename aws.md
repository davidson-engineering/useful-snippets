# AWS S3 Commands
## tags: aws, s3, cli, cloud, cheatsheet
## Copy files to S3 bucket
aws s3 cp . s3://my-bucket/ --recursive --exclude "*" --include "*.txt"
