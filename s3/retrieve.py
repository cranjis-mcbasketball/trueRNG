import boto3
bucket_name = 'haloai'


# Retreive all files bucket
for obj in bucket.objects.all():
    print(obj.key)

# Retreive files of specific folder of bucket
for obj in bucket.objects.filter(Prefix='Input/'):
    print(obj.key)
