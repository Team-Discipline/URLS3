"""
collector.js 를 vultr object storage에 업로드 할 때 쓰는 스크립트 파일.
함부로 실행하지 마시오.
"""

import os

import boto3
from dotenv import load_dotenv

load_dotenv()


def minify_and_uglify():
    ...


def upload_to_bucket():
    hostname = f"{os.getenv('AWS_S3_REGION_NAME')}.{os.getenv('AWS_S3_CUSTOM_DOMAIN')}"
    secret_key = os.getenv('AWS_S3_SECRET_ACCESS_KEY')
    access_key = os.getenv('AWS_S3_ACCESS_KEY_ID')

    session = boto3.session.Session()
    client = session.client('s3', **{
        "region_name": hostname.split('.')[0],
        "endpoint_url": "https://" + hostname,
        "aws_access_key_id": access_key,
        "aws_secret_access_key": secret_key
    })

    # response = client.list_buckets()
    # print(response)

    bucket = os.getenv('AWS_STORAGE_BUCKET_NAME')

    # response = client.list_objects(Bucket=bucket)
    # print(response)

    with open('./js/collector.js', 'rb') as file:
        response = client.put_object(Bucket=bucket, Key='collector.js', Body=file, ACL='private')

    print(response)
