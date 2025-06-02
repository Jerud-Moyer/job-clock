import os
from dotenv import load_dotenv

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

for env_file in ('.env', '.flaskenv'):
  env = os.path.join(os.getcwd(), env_file)
  if os.path.exists(env):
    load_dotenv(env)