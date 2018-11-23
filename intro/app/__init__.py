from flask import Flask
from intro.aws import s3client as s3
from boto3.s3.transfer import S3Transfer
from intro.config.config import get_config

app = Flask(__name__)


s3client = s3.get_s3_client()
cfg = get_config()


@app.route("/")
def hello():
    return "Hello World from Flask"


@app.route('/raca')
def raca():
    return "raca"


@app.route("/buckets")
def get_all_buckets():
    """ :type : pyboto3.s3 """
    for bucket in s3client.list_buckets():
        print(bucket)
    return "ok"


@app.route("/upload")
def upload():
    """ :type : pyboto3.s3 """
    print("starting upload...")
    transfer = S3Transfer(s3client)
    transfer.upload_file('/entrypoint.sh', cfg['bucket_name'], 'file1')
    return "ok"

