import os
from dotenv import load_dotenv

load_dotenv()
# Accessing an environment variable
print(os.environ['HOME'])
print(os.getenv('PORTLINKDME'))