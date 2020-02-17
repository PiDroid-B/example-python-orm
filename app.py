import db


import orm

# import databases
# import sqlalchemy
import asyncio
import functools


def async_adapter(wrapped_func):
    """ Decorator used to run async test cases. """

    @functools.wraps(wrapped_func)
    def run_sync(*args, **kwargs):
        loop = asyncio.get_event_loop()
        task = wrapped_func(*args, **kwargs)
        return loop.run_until_complete(task)

    return run_sync


@async_adapter
async def test1():
    print("script principal")

    db.metadata.create_all(db.engine)

    async with db.database:

        await db.Test1.objects.create(name="toto")
        t = "tassqdfqsdfqsdfsdfqsdfta"

        # print(str(db.Test1.fields["name"].__getattribute__("max_length")))
        t_max = db.Test1.fields["name"].max_length
        print(f"max length of name : {t_max}")

        await db.Test1.objects.create(name=f"{t[:t_max]}")
        all_obj = await db.Test1.objects.all()

    print(type(all_obj))
    print(all_obj)
    print(type(all_obj[0]))
    print(all_obj[0])
    print(type(all_obj[0].name))
    print(all_obj[0].name)

    print("#" * 20)

    async with db.database:

        await db.Test2.objects.create(name="toto", key="key-ok", value=5)
        await db.Test2.objects.create(name="toto2", key="fix-len", value=123456789)

        all_obj = await db.Test2.objects.all()

    print(type(all_obj))
    print(all_obj)
    print(type(all_obj[0]))
    print(all_obj[0])
    print(type(all_obj[0].name))
    print(all_obj[0].name)


test1()
