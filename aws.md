# AWS S3 Commands
## Copy files to S3 bucket
aws s3 cp . s3://my-bucket/ --recursive --exclude "*" --include "*.txt"
