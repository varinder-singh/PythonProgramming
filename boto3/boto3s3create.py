_author_ = "verito"

import boto3
import botocore
s3 = boto3.resource('s3')
inp = input("Do you want to create a s3 bucket in aws? type in y for yes and n for no ").lower()
if inp.__eq__('y'):
    try:
        s3.create_bucket(Bucket='verito0719', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            print("Bucket Not Found!")
        else:
            print("something else have happened {} ".format(e))


   # s3.Object('verito','Analytics Dashboard.pptx').put(Body=open('C:/Users/sandhuv/Desktop/Analytics Dashboard.pptx', 'rb'))
else:
    print("No action is triggered")