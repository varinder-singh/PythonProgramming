import boto3

cf = boto3.client('cloudfront')

cf_list = cf.waiter_names

for name in cf_list:
    print(name)
    if name == "distribution_deployed":
        print("")
