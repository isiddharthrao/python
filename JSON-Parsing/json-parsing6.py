import json
ec2_instance = '{"ID": "i-abcdef", "State": "stopped", "Region": "us-west-2"}'

data = json.loads(ec2_instance)
print(data)
print(f"{data['State']}")