from aiobotocore.config import AioConfig
from aiobotocore.httpsession import AIOHTTPSession
from aiobotocore.httpxsession import HttpxSession
from aiobotocore.utils import AioIMDSFetcher

fetcher = AioIMDSFetcher(env="dev")
fetcher = AioIMDSFetcher(env=None)
fetcher = AioIMDSFetcher(env=123)
config = AioConfig(http_session_cls=AIOHTTPSession)
config = AioConfig(http_session_cls=HttpxSession)
