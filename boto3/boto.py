# Example 1: The "Hello, World!" of boto3 - Listing S3 Buckets
# This is the simplest thing you can do. We ask AWS for a list of all S3 storage buckets in our account.

import boto3
# Replace with your actual credentials
aws_access_key_id = 'ASIAQ72QQZREJJJARWHU'
aws_secret_access_key = 'hOy5a7ZUHunpn6jUG+wQeZ63Z6tDZo0BO3NkC9II'
aws_session_token = 'IQoJb3JpZ2luX2VjEFQaCXVzLWVhc3QtMiJIMEYCIQCmxhwcOZ7WFPYgfhJmKpER/uQf71/Ex+NzprZ3kMkkqQIhAPCHYn/D1ylRKbKJVkKYXxWZYCnOVquIZ+HkjEj7VnyxKq8DCK7//////////wEQAhoMMDY4MzUxNDc4ODU2Igy/wrjWydhSMDlVCEsqgwPlGhfWZ/fEQYchb54nYItdlyWslnK7YVEI5BB/TvwXm4Y+mR9/GGdfNgdBX2vnwDf1EIqHOreZ3sVr2FskOE7xz+/Sm8i0mbqSuJMZ2KYUQg6sNtaLh1uvWJaUUc+xK6iAYddxF7J8a9XiyFvLUNjBab8QugJqNHpqXivKwLXI9wQUPzprnwYZV0wyX4a1tOc88QVIbQEiA7SqnNQkNsTSsUzn2zAQZJEoHRktaZU7ppaCip3rAfrQaIz5QfSG3naKbFumhjTDgaLgB3889MS0v0qqIlDT3BvAGFOPRX727I4lpQ1vPtxMmn5+F7WWGTRYPmM/ZFMUP6RU23Cq8DkuclNmUd+1Kqq8fYZg/iOzs3oNDt3ND/OcaB3ZYpm68mDxxYHbRT3iMVOKAu2RtW5xXgDP/o68+rc7TXQiJtAu+0w6H1yu3ncgI3AOgON4yagp++LscnNtgXORhBi5stelw/rcOOQddp40WsnhGRtXibGrcs0Bi2LRghXJMOw2mm6xP8Qw+/jCxQY6pQEl9dzd+F61kz+av6MbEGXMc/oXdSNoBkYhKwUJJoOdtU2DankX1r2iazU8ZgOQsdoS8jV/bfaEbUFhj927yriE1E4rcH/nPM3ox5QEFQs5AdX28uf/lTdMIaHEmGBdL6tT7kXthVAPGnxAcAXrucUFKUNYkez4m7Yp2ZooAUfjw1WKucl9nfh1imvw4byHezLonabRLdPCshDJqmopRJoVk/Dye8o='  # Only required for temporary credentials
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