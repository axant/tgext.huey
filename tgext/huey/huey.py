from huey import RedisHuey, MemoryHuey, SqliteHuey


class HueyApp:
    instance = None
    consumer = None
    def __init__(self):
        """
        Create an Instance of MemoryHuey [Tests Only]

        Returns:
        MemoryHuey : Instance of MemoryHuey
        """
        if self.instance != None:
            return
        self.instance = MemoryHuey('huey_app')


    def create_consumer(self, **options):
        self.consumer = self.instance.create_consumer(**options)
    

    def start_consumer(self):
        if self.consumer != None:
            self.consumer.start()


    def stop_consumer(self):
        if self.consumer != None:
            self.consumer.stop()
        


class RedisHueyApp(HueyApp):
    def __init__(self, host:str="127.0.0.1", port:str="6379", password=None, db:int=0):
        """
        Create an Instance of RedisHuey
        
        Params:
        host (str) : hostname of the Redis server.
        port (str) : port number of the Redis server.
        password (str) [optional] : password of the Redis server, if any
        db (int): Redis database to use (typically 0-15, default is 0).

        Returns:
        RedisHuey : Instance of RedisHuey
        """
        if self.instance != None:
            return
        self.instance = RedisHuey('huey_app', host=host, port=port)
        if password != None:
            self.instance.password = password


class SqliteHueyApp(HueyApp):
    def __init__(self, cache_mb:int=8, filename:str='huey.db', fsync:bool=False):
        """
        Create an Instance of SqliteHuey
        
        Params:
        host (str) : hostname of the Redis server.
        port (str) : port number of the Redis server.
        fsync (bool) : password of the Redis server, if any

        Returns:
        SqliteHuey : Instance of SqliteHuey
        """
        if self.instance != None:
            return
        self.instance = SqliteHuey('huey_app', filename=filename, cache_mb=cache_mb, fsync=fsync)