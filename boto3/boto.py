# Example 1: The "Hello, World!" of boto3 - Listing S3 Buckets
# This is the simplest thing you can do. We ask AWS for a list of all S3 storage buckets in our account.

import boto3
# Replace with your actual credentials
# aws_access_key_id = ''
# aws_secret_access_key = ''
# aws_session_token = ''  # Only required for temporary credentials
region_name = 'us-east-2' # Specify your desired AWS region

# Step 2: Create an S3 client
s3_client = boto3.client('s3')

# # Step 3: Call the 'list_buckets' method
# response = s3_client.list_buckets()

# # The response is a dictionary. The bucket info is in a list under the 'Buckets' key.
# print("Found the following S3 buckets:")
# for bucket in response['Buckets']:
#     print(f"- {bucket['Name']}")

response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(f"-- {bucket['Name']} created at {bucket['CreationDate']}")