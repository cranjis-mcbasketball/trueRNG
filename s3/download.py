import boto3
# Setup
s3 = boto3.client('s3')

# Download file
bucket_name = 'haloai'
KEY = 's.csv'
s3.Bucket(bucket_name).download_file(KEY, 'local.csv')
