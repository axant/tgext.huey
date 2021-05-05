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
