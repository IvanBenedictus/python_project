import asyncio

async def fetch_data():
    print("start fetching")
    # Get data from server
    await asyncio.sleep(2) 
    print("done fetching")
    return {"data": 1}

async def print_number():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    await asyncio.gather(fetch_data(), print_number())

asyncio.run(main())