import asyncio

import aiohttp

from utils import fetch_status, async_timed, delay


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        failed = 0
        for i, sc in enumerate(status_codes):
            if sc != 200:
                failed += 1
                print(i, sc)
        print('Completed, # Failed requests', failed)


async def out_of_order():
    results = await asyncio.gather(delay(5), delay(1))
    print(results)


asyncio.run(main())
asyncio.run(out_of_order())
