from . import core


import orm


class Test2(orm.Model):
    __tablename__ = "test2"
    __database__ = core.database
    __metadata__ = core.metadata

    id = orm.Integer(primary_key=True)
    name = orm.String(index=True, max_length=30)