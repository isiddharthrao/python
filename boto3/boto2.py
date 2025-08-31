#Describe all ec2 instances using boto3
import boto3
import json
#aws_access_key_id = ''
#aws_secret_access_key = ''
#aws_session_token = ''  # Only required for temporary credentials
region_name = 'us-east-2' # Specify your desired AWS region

# Create an EC2 client
ec2_client = boto3.client('ec2', region_name)

ec2_response = ec2_client.describe_instances()
print(ec2_response)



# try:
#     # Describe all instances
#     response = ec2.describe_instances()

#     # Iterate through reservations and instances
#     for reservation in response['Reservations']:
#         for instance in reservation['Instances']:
#             print(f"Instance ID: {instance['InstanceId']}")
#             print(f"Instance Type: {instance['InstanceType']}")
#             print(f"State: {instance['State']['Name']}")
#             print(f"Launch Time: {instance['LaunchTime']}")
#             print("-" * 20)

# except Exception as e:
#     print(f"Error describing instances: {e}")