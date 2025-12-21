import asyncio
import functools
import time
from typing import Callable, Any

import aiohttp
from aiohttp import ClientSession


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f'starting {func.__name__}() with args {args} {kwargs}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                total = time.time() - start
                print(f'finished {func.__name__}() in {total:.4f} second(s)')

        return wrapped

    return wrapper


@async_timed()
async def delay(delay_seconds: int) -> int:
    print(f'sleeping for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    print(f'finished sleeping for {delay_seconds} second(s)')
    return delay_seconds


async def fetch_status(session: ClientSession,
                       url: str,
                       timeout: int = 0,
                       delay: int = 0) -> int:
    if delay:
        await asyncio.sleep(delay)

    if timeout:
        # Set a request timeout of 100 ms for particular request
        request_timeout = aiohttp.ClientTimeout(total=timeout)
        async with session.get(url, timeout=request_timeout) as result:
            return result.status

    async with session.get(url) as result:
        return result.status
