# workaraund to work with external folders modules
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from pydantic import BaseSettings


class Settings(BaseSettings):
    rabbitmq_user: str = 'testing'
    rabbitmq_pass: str = 'testing'
    rabbitmq_host: str = '3.222.131.105'
    rabbitmq_port: int = 5673
    my_queue: str = "cuarto_electrico"


SETTINGS = Settings()
