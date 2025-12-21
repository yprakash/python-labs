import asyncio

import aiohttp

from utils import fetch_status


async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        exceptions = [res for res in results if isinstance(res, Exception)]
        normal = [res for res in results if not isinstance(res, Exception)]
        print(f'All results: {results}')
        print(f'Finished successfully: {normal}')
        print(f'Threw exceptions: {exceptions}')


asyncio.run(main())
