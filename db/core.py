import databases
import sqlalchemy
import orm
import typesystem


def get_url():
    url = "sqlite:///test.db"
    return url


# custom field type : BigInt
class BigInt(orm.fields.ModelField, typesystem.Integer):
    def get_column_type(self):
        return sqlalchemy.BIGINT()


# custom field type : Char
class Char(orm.fields.ModelField, typesystem.String):
    def get_column_type(self):
        return sqlalchemy.CHAR(length=self.max_length)


database = databases.Database(get_url(), force_rollback=True)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(get_url())
