import os
import json
import botocore.exceptions
import logging
import requests

s3_client = boto3.client("s3")
S3_BUCKET = os.getenv("S3_BUCKET")

#Function to get a file from url with a try and exception

