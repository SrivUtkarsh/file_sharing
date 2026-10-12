import boto3
import os
from botocore.config import Config
s3=boto3.client(
    "s3",
    endpoint_url=os.getenv(
        "S3_ENDPOINT_URL",
        "http://localhost:8333"
    ),
    aws_access_key_id= os.getenv("S3_ACCESS_KEY", "devuser"),
    aws_secret_access_key=os.getenv(
        "S3_SECRET_KEY",
        "DevStoragePass123!"
    ),
    region_name="ap-south-1",
    config=Config(
        s3={"addressing_style":"path"}
    )
)
BUCKET="app-files"
def upload_file(file,key,content_type):
    s3.upload_fileobj(
        file,BUCKET,
        key,
        ExtraArgs={"ContentType":content_type or "application/octet-stream"}
    )
def download_file(key):
    return s3.get_object(
        Bucket=BUCKET,
        Key=key
    )