class CarlaClient:

    """

    Thin wrapper around a future CARLA Python client.

    CARLA runs as a separate simulator server.

    Aegis connects to it, reads camera frames,

    runs perception models, applies attacks, and evaluates failures.

    """

    def __init__(self, host: str = "localhost", port: int = 2000):

        self.host = host

        self.port = port

    def connect(self):

        raise NotImplementedError("CARLA server connection will be added later.")