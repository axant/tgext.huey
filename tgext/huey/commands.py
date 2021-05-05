from gearbox.command import Command
from os import getcwd
from paste.deploy import loadapp
from tg import config

import logging
log = logging.getLogger('tgext.huey')


class HueyWorkerCommand(Command):
    def get_description(self):
        return "Starts Huey worker in turbogears"

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)

        parser.add_argument("-c", "--config",
                            help='application config file to read (default: development.ini)',
                            dest='config_file', default="development.ini")

        parser.add_argument('-w', '--workers',
                            help='number of workers created by the consumer', default='1', dest='workers')

        parser.add_argument('-l', '--logfile',
                            help='path of the log file', default='huey_log.txt')

        parser.add_argument('-L', '--loglevel',
                            help='severity of the log', default='INFO')

        return parser

    def take_action(self, opts):
        from tgext.huey.huey import HueyApp
        config_file = opts.config_file
        workers = opts.workers
        config_name = 'config:%s' % config_file
        here_dir = getcwd()

        # Load the wsgi app first so that everything is initialized right
        loadapp(config_name, relative_to=here_dir)
        huey_type = config['huey_configuration_object'].get('TYPE', "base")
        huey = None

        if huey_type is 'redis':
            address = config['huey_configuration_object'].get('ADDRESS', "127.0.0.1")
            port = config['huey_configuration_object'].get('PORT', "6379")
            password = config['huey_configuration_object'].get('PASSWORD', None)
            db = config['huey_configuration_object'].get('DB', 0)
            huey = RedisHueyApp(
                address=address,
                port=port,
                password=password,
                db=db
            )

        if huey_type is 'sqlite':
            filename = config['huey_configuration_object'].get('FILENAME', "huey.db")
            cache_mb = config['huey_configuration_object'].get('CACHE_MB', 8)
            fsync = config['huey_configuration_object'].get('FSYNC', False)
            huey = SqliteHueyApp(
                filename=filename,
                cache_mb=int(cache_mb),
                fsync=fsync
            )

        if huey_type not in ['redis', 'sqlite']:
            huey = HueyApp()
        huey.create_consumer(workers=int(workers))
        log.info("Consumer created!")