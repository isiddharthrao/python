# Example 1: A simple JSON object
# This is a string containing JSON data. We'll parse it into a Python dictionary.

import json

# This is a JSON string (notice the quotes around the whole thing)
user_json_string = '{"userId": "user123", "username": "alex", "isActive": true}'

# Parse the string into a Python dictionary
parsed_json = json.loads(user_json_string)

print(f"Username is: {parsed_json['username']}")
print(f"User ID is: {parsed_json['userId']}")
print(f"User Activity is: {parsed_json['isActive']}")