import boto3
from intro.config import config

s3client = boto3.client(
    's3',
    aws_access_key_id=config.get_config().get('access_key'),
    aws_secret_access_key=config.get_config().get('secret_key'),
)
""" :type : pyboto3.s3 """