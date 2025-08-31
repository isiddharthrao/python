# Example 2: A nested JSON object
# Often, a JSON object will contain another object inside it.
import json
instance_json_string = '''
{
  "InstanceId": "i-12345",
  "Details": {
    "State": "running",
    "Region": "us-east-1"
  }
}
'''
parsed_instance_data = json.loads(instance_json_string)
#print(parsed_instance_data)
# To get a nested value, you access it step-by-step
#print(f"The instance is in region: {instance_data['Details']['Region']}")
print(f"The instance id {parsed_instance_data['InstanceId']}is in region: {parsed_instance_data['Details']['Region']}")
