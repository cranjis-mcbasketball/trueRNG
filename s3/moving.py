import boto3
# Setup
s3 = boto3.client('s3')

# Copying file from one bucket to other
bucket_name = 'haloai'
copy_source = {
    'Bucket': 'haloai',
    'Key': 's1.csv'
}

dest_bucket_name = 'haloai'
dest_key = 'Input/s2.csv'
s3.meta.client.copy(copy_source, dest_bucket_name, dest_key)
