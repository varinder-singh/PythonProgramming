import boto3
import botocore

# point to boto3 resource 's3'
s3 = boto3.resource('s3')
# pass the bucket name
bucket = s3.Bucket('verito0719')

exist = True
# look for bucket
try:
    s3.meta.client.head_bucket(Bucket = 'verito0719')
except botocore.exceptions.ClientError as e:
    error_code = e.response['Error']['Code']
    if error_code == '404':
        exist = False
        print("Bucket Not Found!!!")
    else:
        print("Cannot determine what happened Code is - {}".format(e))
print("Bucket name is : {}".format(bucket.name))