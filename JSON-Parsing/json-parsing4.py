# Example 4: A list of JSON objects
# Sometimes the entire JSON payload is a list of objects. This is how you'd get a list of users or EC2 instances from an API.

import json

users_json_string = '''
[
  {"username": "alex", "role": "admin"},
  {"username": "brian", "role": "editor"},
  {"username": "casey", "role": "viewer"}
]
'''
users_list = json.loads(users_json_string)

# The result is a Python list of dictionaries
# print("User Roles:")
# for user in users_list:
#     print(f"{user['username']} has the role: {user['role']}")

parsed_user_json_string = json.loads(users_json_string)
print("User roles are as follows: ")
for user_role in parsed_user_json_string:
    print(f"{user_role['username']} has access to {user_role['role']}.")
