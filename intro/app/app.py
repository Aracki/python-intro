from boto3.s3.transfer import S3Transfer
import boto3
import yaml

from intro.app import app

global s3client

print('app.py from app/')

def init_s3():
    s3client = boto3.client(
        's3',
        aws_access_key_id=conf['access_key'],
        aws_secret_access_key=conf['secret_key'],
    )
    """ :type : pyboto3.s3 """


def read_configuration():
    with open("prop.yaml", 'r') as stream:
        try:
            global conf
            conf = yaml.load(stream)
            print(conf['access_key'])
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4446, threaded=True, debug=True)


@app.route("/")
def hello():
    return "Hello World from Flask"


# @app.route("/raca")
# def raca():
#     return "Hello Raca"


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
    transfer.upload_file('fly_to_s3.txt', conf['bucket_name'], 'file1')
    return "ok"
