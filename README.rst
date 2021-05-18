About tgext.huey
-------------------------

tgext.huey is a TurboGears2 extension

Installing
-------------------------------

tgext.huey can be installed from pypi::

    pip install tgext.huey

should just work for most of the users.

Enabling
-------------------------------

To enable tgext.huey put inside your application
``config/app_cfg.py`` the following::

    import tgext.huey
    tgext.huey.plugme(base_config)

or you can use ``tgext.pluggable`` when available::

    from tgext.pluggable import plug
    plug(base_config, 'tgext.huey')


Usage
-------------------------------

To use tgext.huey create a huey instance using one of the following options::
    
    # SQlite
    from tgext.huey.huey import SqliteHueyApp
    huey = SqliteHueyApp()
    # This is equivalent to
    huey = SqliteHueyApp(
        filename="huey.db",
        cache_mb=8,
        fsync=False
    )

    # Redis
    from tgext.huey.huey import RedisHueyApp
    huey = RedisHueyApp()
    # This is equivalent to
    huey = RedisHueyApp(
        host="127.0.0.1",
        port="6379",
        password=None,
        db=0
    )

    # MemoryHuey
    from tgext.huey.huey import HueyApp
    huey = HueyApp()
    # This option is meant to be used during tests.

When you have created your HueyApp you can create and start the consumer using::

    huey.start_consumer(workers=2)
    # This will create (if it doesn't exists) 
    # and start a consumer that will use 2 workers

If you want to stop the consumer you can just use::

    huey.stop_consumer()
    # This will stop the consumer

Here is an example of periodic and simple tasks::

    # Simple task
    @huey.instance.task()
    def add(a, b):
        return a + b

    # Periodic Task
    from huey import crontab
    @huey.instance.periodic_task(crontab(minute='*/3'))
    def every_three_minutes():
       print('This task runs every three minutes')