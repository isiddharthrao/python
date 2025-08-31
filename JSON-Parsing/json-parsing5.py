# Example 5: A more realistic, complex example
# This mimics a response from AWS. We'll pull out multiple pieces of information.

import json

ec2_json_string = '''
{
    "Reservations": [
        {
            "Instances": [
                {
                    "InstanceId": "i-0e8fae83c2738733f",
                    "InstanceType": "t2.micro",
                    "State": {
                        "Name": "running"
                    },
                    "SecurityGroups": [
                        {
                            "GroupName": "launch-wizard-1",
                            "GroupId": "sg-0a1b2c3d4e5f67890"
                        }
                    ]
                }
            ]
        }
    ]
}
'''
parsed_ec2_data = json.loads(ec2_json_string)
#print(parsed_ec2_data)
print(f"Instance ID: {parsed_ec2_data["Reservations"][0]['Instances'][0]['InstanceId']}")
print(f"Instance State is {parsed_ec2_data['Reservations'][0]['Instances'][0]['State']['Name']}")

sg = parsed_ec2_data['Reservations'][0]['Instances'][0]['SecurityGroups'][0]
print(f"Security group is {sg['GroupId']}")

# ec2_data = json.loads(ec2_json_string)

# # To get to the data we want, we have to go through the structure
# instance_details = ec2_data["Reservations"][0]["Instances"][0]

# instance_id = instance_details["InstanceId"]
# instance_type = instance_details["InstanceType"]
# instance_state = instance_details["State"]["Name"]

# print(f"Instance ID: {instance_id}")
# print(f"Instance Type: {instance_type}")
# print(f"Instance State: {instance_state}")