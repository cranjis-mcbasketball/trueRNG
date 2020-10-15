import boto3
# DELETE
obj = bucket.Object(key='Input/s2.csv')
obj.delete()
