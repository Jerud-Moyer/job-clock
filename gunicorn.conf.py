import os
from dotenv import load_dotenv

max_requests = 1000
max_requests_jitter = 50

log_file = "-"

for env_file in ('.env', '.flaskenv'):
  env = os.path.join(os.getcwd(), env_file)
  if os.path.exists(env):
    load_dotenv(env)

uri = os.getenv("DATABASE_URL")
print('HERE IT IS!!!! ')
print(uri)
if uri.startswith("postgres://"):
    print('DO WE EVEN GET IT HERE THOUGH???')
    uri = uri.replace("postgres://", "postgresql://", 1)
    print(uri)