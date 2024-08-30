from typing import Any, Dict, Mapping, Optional

from aiobotocore.credentials import AioCredentials
from botocore.utils import DEFAULT_METADATA_SERVICE_TIMEOUT as DEFAULT_METADATA_SERVICE_TIMEOUT
from botocore.utils import METADATA_BASE_URL as METADATA_BASE_URL
from botocore.utils import (
    ContainerMetadataFetcher,
    IdentityCache,
    IMDSFetcher,
    IMDSRegionProvider,
    InstanceMetadataFetcher,
    InstanceMetadataRegionFetcher,
    S3ExpressIdentityCache,
    S3ExpressIdentityResolver,
    S3RegionRedirector,
    S3RegionRedirectorv2,
)
from requests.models import Response

logger: Any
RETRYABLE_HTTP_ERRORS: Any

class AioIMDSFetcher(IMDSFetcher):
    def __init__(
        self,
        timeout: int = ...,
        num_attempts: int = ...,
        base_url: str = ...,
        env: Optional[str] = ...,
        user_agent: Optional[str] = ...,
        config: Optional[Any] = ...,
        session: Optional[Any] = ...,
    ) -> None: ...

class AioInstanceMetadataFetcher(AioIMDSFetcher, InstanceMetadataFetcher):
    async def retrieve_iam_role_credentials(self) -> Dict[str, Any]: ...

class AioIMDSRegionProvider(IMDSRegionProvider):
    async def provide(self) -> str: ...

class AioInstanceMetadataRegionFetcher(AioIMDSFetcher, InstanceMetadataRegionFetcher):
    async def retrieve_region(self) -> Optional[str]: ...  # type: ignore [override]

class AioIdentityCache(IdentityCache):
    async def get_credentials(self, **kwargs: Any) -> AioCredentials: ...  # type: ignore [override]

class AioS3ExpressIdentityCache(AioIdentityCache, S3ExpressIdentityCache):
    async def get_credentials(self, bucket: str) -> AioCredentials: ...  # type: ignore [override]

class AioS3ExpressIdentityResolver(S3ExpressIdentityResolver): ...

class AioS3RegionRedirectorv2(S3RegionRedirectorv2):
    async def redirect_from_error(
        self,
        request_dict: Mapping[str, Any],
        response: Response,
        operation: Any,
        **kwargs: Any,
    ) -> None: ...
    async def get_bucket_region(self, bucket: Any, response: Response) -> Any: ...

class AioS3RegionRedirector(S3RegionRedirector):
    async def redirect_from_error(
        self, request_dict: Mapping[str, Any], response: Response, operation: Any, **kwargs: Any
    ) -> Optional[int]: ...
    async def get_bucket_region(self, bucket: str, response: Response) -> str: ...

class AioContainerMetadataFetcher(ContainerMetadataFetcher):
    def __init__(self, session: Optional[Any] = ..., sleep: Any = ...) -> None: ...
    async def retrieve_full_uri(self, full_url: str, headers: Optional[Any] = ...) -> str: ...
    async def retrieve_uri(self, relative_uri: str) -> Any: ...
