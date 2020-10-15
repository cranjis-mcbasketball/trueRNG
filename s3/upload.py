import boto3
import os
# Setup
s3 = boto3.client('s3')
# Upload file
src_folder = './NED_BYTES/'
dest_folder = '/'
bucket_name = 'haloai2'
for file in os.listdir(src_folder):
    s3.upload_file(src_folder+file, bucket_name, file)
