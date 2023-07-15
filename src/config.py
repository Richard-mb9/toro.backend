from decouple import config
from dotenv import load_dotenv, find_dotenv
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

ENVIRONMENT = config("ENVIRONMENT", default="test")
dotenv = find_dotenv(f".env.{ENVIRONMENT.lower()}")
load_dotenv(dotenv)


HOST_DB = config("HOST_DB", default=None)
PASSWORD_DB = config("PASSWORD_DB", default=None)
USER_DB = config("USER_DB", default=None)
NAME_DB = config("NAME_DB", default=None)
PORT_DB = int(config("PORT_DB", default=None))

SECRETKEY = config("SECRETKEY", None)
EXP_TIME_MIN = int(config("EXP_TIME_MIN", None))

Base: DeclarativeMeta = declarative_base()
