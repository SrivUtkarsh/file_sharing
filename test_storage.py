import boto3
from botocore.config import Config
s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:8333",
    aws_access_key_id="devuser",
    aws_secret_access_key="DevStoragePass123!",
    region_name="ap-south-1",
    config=Config(s3={"addressing_style": "path"})
)
s3.put_object(
    Bucket="app-files",
    Key="hello.txt",
    Body=b"Hello from FastAPI project",
    ContentType="text/plain"
)
print("Uploaded successfully")
result = s3.get_object(
    Bucket="app-files",
    Key="hello.txt"
)
content = result["Body"].read().decode("utf-8")
print("Downloaded content:", content)