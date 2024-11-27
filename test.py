from aiobotocore.utils import AioIMDSFetcher

fetcher = AioIMDSFetcher(env="dev")
fetcher = AioIMDSFetcher(env=None)
fetcher = AioIMDSFetcher(env=123)
