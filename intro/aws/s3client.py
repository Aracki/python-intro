import pyboto3.s3
import boto3
from intro.config.config import get_config

cfg = get_config()


def get_s3_client():
    return boto3.client(
        's3',
        aws_access_key_id=cfg['access_key'],
        aws_secret_access_key=cfg['secret_key'],
    )


test_s3_client = get_s3_client()
""":type: pyboto3.s3 """
# test_s3_client.list_buckets()
# autocomplete works here
