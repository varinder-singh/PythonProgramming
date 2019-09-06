import boto3


def checkMaintenceEc2():
    ec2 = boto3.client('ec2', region_name='eu-central-1')
    response = ec2.describe_instances(  Filters=[
        {
            'Name': 'image-id',
            'Values': [
                'ami-938d8178',
            ]
        },
        {
            'Name':'tag:Role',
            'Values': ['uiweb-maintenance']
        }
    ])
    if len(response['Reservations']) != 0:
        #print("The intances are ")
    for x in response['Reservations']:
        #print(x)
        for item in x['Instances']:
            print("The Instance ID is {}".format(item['InstanceId']))
            print("Private IP Address {}".format(item['PrivateIpAddress']))
    else:
        print("The list returned is null")


if __name__=="__main__":
    checkMaintenceEc2()