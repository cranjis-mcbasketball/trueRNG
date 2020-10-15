import boto3
import os
import time
# Setup
s3 = boto3.client('s3')


def updateTrueRNGDatas3():
    while True:
        # Delete trueRNG data from data/ directory
        BUCKET = 'haloai2'
        PREFIX = 'data/'

        response = s3.list_objects_v2(Bucket=BUCKET, Prefix=PREFIX)

        for object in response['Contents']:
            print('Deleting', object['Key'])
            s3.delete_object(Bucket=BUCKET, Key=object['Key'])
        time.sleep(5)
        # Upload new trueRNG data to s3 bucket
        src_folder = './NED_BYTES/'
        dest_folder = 'data/'
        bucket_name = 'haloai2'
        for file in os.listdir(src_folder):
            print('Uploading', dest_folder+file)
            s3.upload_file(src_folder+file, bucket_name, dest_folder+file)
        # replace the "600" with however many seconds the program should wait before doing another data update
        time.sleep(600)


updateTrueRNGDatas3()
