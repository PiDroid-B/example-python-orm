import db


# import orm
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
        await db.Test1.objects.create(name="tata")

        all_obj = await db.Test1.objects.all()

    print(all_obj)


test1()
