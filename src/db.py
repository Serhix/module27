import configparser
import pathlib

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

username = config.get("DB_DEV", "USER")
password = config.get("DB_DEV", "PASSWORD")
database_name = config.get("DB_DEV", "DB_NAME")
host = config.get("DB_DEV", "HOST")
port = config.get("DB_DEV", "PORT")
url = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"

engine = create_engine(url, echo=False, pool_size=5)
Session = sessionmaker(bind=engine)
session = Session()
