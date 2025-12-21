import asyncio

import aiohttp

from utils import fetch_status, async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [fetch_status(session, 'https://www.example.com', 15, 10),
                    fetch_status(session, 'https://www.example.com', 10, 5),
                    fetch_status(session, 'https://www.example.com', 5, 1)]

        for finished_task in asyncio.as_completed(fetchers, timeout=10):
            try:
                result = await finished_task
                print(result)
            except asyncio.TimeoutError:
                print('We got a timeout error!')

        for task in asyncio.all_tasks():
            print(task)


asyncio.run(main())
