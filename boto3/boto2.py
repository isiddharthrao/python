#Describe all ec2 instances using boto3
import boto3
import json
aws_access_key_id='ASIAWYXBQ5HFU7RNJE23'
aws_secret_access_key='J0Brw7FHtJPC5HrR9/RuBQmcVFsIj0EgQ9vZHnpt'
aws_session_token='IQoJb3JpZ2luX2VjEGEaCXVzLWVhc3QtMiJHMEUCIQCiECxHLpjOwk5Uce/EHAu9WF4JWD2hKiaB2Br9cSgaKAIgTje9ih6nIrnn/bAkQ6ZVaVlmSBK71ClJ1dJgsdG5mQ4qrwMIuv//////////ARAAGgw0NjU0MDMxNzc0MTkiDGlbRxJD8Gt5+8S49iqDA+28u3OwefwDWwmXB2dLFvIxLJih+TTneLAVFCqEphT3EO1LSPpl3Hyhc+2QBZQ5e7fQwmBrf8P3wy6iE7lWV2lRzQpqmVOI4qpLApJMa7Z4/nR0YsSDVQMMH18aMDRH0oAFM1RhIJ5qrhMTjjWlFja83KXyIcvA3owboA7svnx7eCK+fbtifzgJdDHWQPirqPtJwdXThjDP10c7fcvZbJa6CYy/yzDt7iwPu9j+jeo6uaBk1KxD0wvcUoU/0rpDUVOOc7YgFAzlH3pIAd+OB1z++VIe4hHfmzgTqDnSAwyfO3gPIahOKV8oIufEDenI/62T3wWPiB5GqXb1n0CQQhXNSqviWo7pF90L1eQNF893PvSdtRODBoUwGclUvbSc8PgZtagjtl5wG7rPSZ6OYuB8Brdq8NZi0GEy0LVZ6kcxDvdFo/uDfpNSj639dxua64gJJREO+XzR89kAXv7igzwpP8scNotyWQ9TRCGMG7L1fz9x/Cm8GHJks146grDVS4Qd5zC608XFBjqmAVSYtnE9le5k2AxFI6ZTGKUv0ZtJJXIe+kDw1/oE96GOJrdgou5d26PfoFxYPODmy0f8nxPdS9iCrhP7x/ImEQWCZz8zzsi8GSobDthdQQDmGvqp64iXiSy41QSC6TaLYwZcyRiIMDTgEfH4Ziy0dA62u1VgzdmicCb/AqxUNx1Hc3NUdngwd/AGbNm1OSxSr027oFXu8RTjOt3mN83uPT6GcGB6BTo='
region_name = 'us-east-1' # Specify your desired AWS region

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