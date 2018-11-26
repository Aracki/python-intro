# python-intro
Introduction to Python with Docker. Flask web app. Uploads to S3. SQLAlchemy. 

## Prerequisites

1. `docker` & `docker-compose` installed.
2. Create `aws-config.yml` in the root of the project based on the template given.


## PyCharm settings

1. Set up docker's remote python interpreter 
2. After adding a new package to requirements.txt you will need to rerun container and restart PyCharm

## Deployment

1. `docker build -t python-intro docker`
2. `docker-compose up`
