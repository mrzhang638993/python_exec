# 测试python的异步io机制,实现更加高效的异步代码操作实现。
import asyncio
import time


async def hi(i):
    # 做复杂耗时的操作
    await asyncio.sleep(i)
    print("i am  {} ".format(i))


async def main():
    start = time.time()
    task = []
    for i in range(1, 5):
        task += asyncio.ensure_future(hi(i))
    print(" main method  end")
    print(time.time() - start)
    return task


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
