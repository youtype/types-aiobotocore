"""
Copyright 2024 Vlad Emelianov
"""

from typing import Any

from aiobotocore.httpsession import AIOHTTPSession
from botocore.config import Config
from typing_extensions import Self

class AioConfig(Config):
    def __init__(
        self, connector_args: Any = ..., http_session_cls: type[AIOHTTPSession] = ..., **kwargs: Any
    ) -> None: ...
    def merge(self, other_config: Config) -> Self: ...
