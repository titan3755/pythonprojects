import asyncio


async def test_func():
    print('wassap')
    task = asyncio.create_task(weed())
    await task
    print('finished')


async def weed():
    print('Akij bhai ganza bhai')
    await asyncio.sleep(2)

asyncio.run(test_func())