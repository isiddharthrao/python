# Example 3: JSON containing a list
# A very common pattern. Here, the tags key holds a list of strings.

import json

server_json_string = '''
{
  "ServerName": "WebApp01",
  "ip_address": "192.168.1.10",
  "tags": ["web", "production", "nginx"]
}
'''
server_data = json.loads(server_json_string)

# We can access the list and then loop through it!
# print("Server tags:")
# for tag in server_data['tags']:
#     print(f"- {tag}")

print("Server tags: ")
for env_tag in server_data['tags']:
    print(f"-- {env_tag}")

print(f"{server_data['tags']}")