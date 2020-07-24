# account demo
from client import Client
from config import Config
from enums import EnvironmentEnum
from seerbit import Seerbit
from service.authentication import Authentication


def authenticate() -> str:
    """ User authentication token """
    print("================== start authentication ==================")
    client = Client()
    seerbit = Seerbit()
    client.api_base = seerbit.LIVE_API_BASE
    client.environment = EnvironmentEnum.LIVE.value
    config = Config()
    config.put("public_key", "public2key")
    config.put("private_key", "private2key")
    client.config = config
    client.timeout = 20
    auth_service = Authentication(client)
    response = auth_service.auth()
    print("environment: " + client.environment)
    print("response: " + str(response))
    print("================== end authentication ==================")
    return auth_service.get_token()


token = authenticate()
print("token: " + token)
