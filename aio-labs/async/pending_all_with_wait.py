import asyncio
from collections import deque

import aiohttp

from utils import fetch_status


async def main():
    urls = ['https://www.example.com' for _ in range(5)]
    q_len = 3
    async with aiohttp.ClientSession() as session:
        all_tasks = [asyncio.create_task(fetch_status(session, url))
                     for url in urls]
        pending = deque()
        for _ in range(q_len):
            pending.append(all_tasks.pop(0))

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')

            for done_task in done:
                print(await done_task)
            if all_tasks:
                pending.add(all_tasks.pop(0))


asyncio.run(main())
