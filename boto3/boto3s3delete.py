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
        exit()
    else:
        print("Cannot determine what happened Code is - {}".format(e))
# take the input from the user to delete the bucket
inp = input("Are you sure you want to delete a bucket y for yes and n for no")
if inp == 'y':
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()
print("Bucket deleted successfully please go n check the aws console")