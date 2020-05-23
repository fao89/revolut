import os
from dotenv import load_dotenv
import sqlalchemy
import sqlalchemy_utils

load_dotenv()


def create_database():
    conn_str = "postgresql+psycopg2://{}:{}@{}:5433/{}".format(
        os.environ.get("POSTGRES_USER"),
        os.environ.get("POSTGRES_PASS"),
        os.environ.get("POSTGRES_HOST"),
        os.environ.get("POSTGRES_DB"),
    )

    engine = sqlalchemy.create_engine(conn_str)
    sqlalchemy_utils.create_database(engine.url)


if __name__ == "__main__":
    create_database()
