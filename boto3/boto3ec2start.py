_author_ = "verito"

# The below program will connect to my aws account as it used .aws folder which has root key and root password.
# The below boto3 agent will connect, first lists and then based on the consent will stop the ec2 instance under this account.
# Have provided the aws root key and password using aws cli command

import boto3

# Boto 3
# Use the filter() method of the instances collection to retrieve
# all running EC2 instances.


ec2 = boto3.resource('ec2')
instanceId = []
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
for instance in instances:
    instanceId.append(instance.id)
    print("Instance ID : {0} and Instance Type : {1} ".format(instance.id, instance.instance_type))

# action to stop the ec2 instance
inp = input("Do you want to start the only running ec2 instance yes or quit? ").lower()

if inp == 'yes':
    ec2.instances.filter(InstanceIds=instanceId).start()
else:
    print("you quit!")
