import boto3
from intro.config.config import get_config


def get_s3_client():
    s3client = boto3.client(
        's3',
        aws_access_key_id=get_config()['access_key'],
        aws_secret_access_key=get_config()['secret_key'],
    )