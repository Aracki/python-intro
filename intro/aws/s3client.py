import boto3
from intro.config.config import get_config

cfg = get_config()


def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=cfg['access_key'],
        aws_secret_access_key=cfg['secret_key'],
    )
