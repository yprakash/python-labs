import asyncio
from asyncio import CancelledError, Future

from utils import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(2)
    return 'Hello World!'


async def main2() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(message)
    print(one_plus_one)


async def main3():
    sleep_for_three = asyncio.create_task(delay(3))
    print(type(sleep_for_three))
    await delay(1)
    print(await add_one(1))
    result = await sleep_for_three
    print(result)


async def main4():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(2))
    sleep_once_more = asyncio.create_task(delay(1))
    await sleep_for_three
    print('Done 3 sleep_for_three')
    await sleep_again
    print('Done 2 sleep_again')
    await sleep_once_more
    print('Done 1 sleep_once_more')


async def cancel_demo():
    long_task = asyncio.create_task(delay(5))
    seconds_elapsed = 0

    while not long_task.done():
        await asyncio.sleep(1)
        seconds_elapsed += 1
        print('%d seconds elapsed but long task Not done yet' % seconds_elapsed)
        if seconds_elapsed == 3:
            long_task.cancel()

    try:
        await long_task
        print('long_task has been completed')
    except CancelledError:
        print('long_task has been cancelled')


async def wait_for_demo():
    delay_task = asyncio.create_task(delay(5))
    try:
        await asyncio.wait_for(delay_task, timeout=1)
    except asyncio.exceptions.TimeoutError as e:
        print('Got timeout ', e)
        print(f'Was the task cancelled? {delay_task.cancelled()}')


async def shield_demo(total_time=10, shield_time=5):
    task = asyncio.create_task(delay(total_time))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=shield_time)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("TimeoutError with shield. Task took longer than expected, it will finish soon!")
        res = await task
        print(res)


def make_request(request_time=2, result=10) -> Future:
    async def set_future_value(f) -> None:
        await delay(request_time)
        f.set_result(result)

    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def futures_demo():
    future = make_request(2)
    print(f'Is the future done? {future.done()}')
    value = await future
    print(f'Is the future done? {future.done()}')
    print(value)


async def main():
    # await main2()
    await main3()
    # await cancel_demo()
    # await wait_for_demo()
    # await shield_demo()
    # await futures_demo()

asyncio.run(main())
print('Exiting..')
