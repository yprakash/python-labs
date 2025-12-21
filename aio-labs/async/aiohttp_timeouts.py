import asyncio

import aiohttp

from utils import fetch_status


async def main():
    # Set total timeout of 10 seconds and explicitly set a connection timeout of 1 second
    session_timeout = aiohttp.ClientTimeout(total=10, connect=1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        code = await fetch_status(session, 'https://example.com')
        print('Response:', code)


asyncio.run(main())
