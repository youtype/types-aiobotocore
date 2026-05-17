"""
Type annotations for aiobotocore.config module.

Copyright 2025 Vlad Emelianov
"""

from types import TracebackType
from typing import Any, Protocol, TypeVar

from aiobotocore.awsrequest import AioAWSResponse
from botocore.awsrequest import AWSPreparedRequest
from botocore.config import Config

_Config = TypeVar("_Config", bound=Config)

DEFAULT_KEEPALIVE_TIMEOUT: int = ...
TIMEOUT_ARGS: frozenset[str] = ...

_R = TypeVar("_R")

class _HTTPSessionProtocol(Protocol):
    def __init__(
        self,
        verify: bool = ...,
        proxies: dict[str, str] | None = ...,
        timeout: float | None = ...,
        max_pool_connections: int = ...,
        socket_options: list[Any] | None = ...,
        client_cert: str | tuple[str, str] | None = ...,
        proxies_config: dict[str, str] | None = ...,
        connector_args: dict[str, Any] | None = ...,
    ) -> None: ...
    async def __aenter__(self: _R) -> _R: ...
    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
    async def close(self) -> None: ...
    async def send(self, request: AWSPreparedRequest) -> AioAWSResponse: ...

class AioConfig(Config):
    def __init__(
        self,
        connector_args: Any = ...,
        http_session_cls: type[_HTTPSessionProtocol] = ...,
        **kwargs: Any,
    ) -> None: ...
    def merge(self: _Config, other_config: _Config) -> _Config: ...
