# Function can be used by a CloudWatch Event Rule
import boto3

# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g.; 'eu-west-1'
region = 'eu-west-1'
# Enter your instances here: ex. 'testdb'
instance = 'testdb'

client = boto3.client('rds')

def lambda_handler(event, context):
    rds = boto3.client('rds', region_name=region)
    client.start_db_instance(DBInstanceIdentifier=instance)
    print 'started your instance: ' + str(instance)