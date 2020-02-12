import databases
import sqlalchemy


def get_url():
    url = "sqlite:///test.db"
    return url


database = databases.Database(get_url(), force_rollback=True)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(get_url())

