FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip install boto3 && \
    pip install pyboto3 && \
    pip install pyyaml

COPY ./app /app
