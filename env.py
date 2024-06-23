import os
from dotenv import load_dotenv
import boto3
load_dotenv()
# Accessing an environment variable
print(os.environ['HOME'])
print(os.getenv('PORTLINKDME'))


s3_client = boto3.client('s3', aws_access_key_id="AKIA6GBMHU2LMLGXDWUD", aws_secret_access_key= "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", config= boto3.session.Config(signature_version='v4', region_name = 'us-east-2',))
response =s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': "linkdmebucket",
                                                            'Key': "hello1.png"},
                                                    ExpiresIn=360)
#response = s3_client.upload_file("image.png", "linkdmebucket", "hello1.png")
#print(response)
#response= s3_client.get_object(Bucket="linkdmebucket",Key="hello1.png")
#response = s3_client.download_file("linkdmebucket", "hello1.png", "test.png")
print(response)