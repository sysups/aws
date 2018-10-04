# Function can be used by a CloudWatch Event Rule

import boto3
# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g., 'eu-west-1'
region = 'eu-west-1'
# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['X-XXXXXXXX']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    print 'stopped your instances: ' + str(instances)
