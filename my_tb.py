import asyncio
import sys
import traceback


async def m(i):
    try:
        await asyncio.sleep(1)
        assert i != 5, '不要5'
        return 1 / i
    except Exception as E:
        raise E


async def main():
    try:
        tasks = list()
        for i in range(10):
            tasks.append(m(i))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        for res in results:
            if isinstance(res, Exception):
                tb_string = ''.join(traceback.format_tb(res.__traceback__))
                print(f"幹! 出錯了 \n{tb_string}")

            else:
                print(res)

    except Exception as E:
        print(traceback.format_exc())
        raise E


if __name__ == '__main__':
    asyncio.run(main())
