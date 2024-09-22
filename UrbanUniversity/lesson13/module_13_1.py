import asyncio


async def start_strongman(name, power):
    print(f"Strongman {name} started competitions")

    for i in range(1, power + 1):
        await asyncio.sleep(1)
        print(f"Strongman {name} lifted ball {i}")

    print(f"Strongman {name} finished competitions")


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))

    await task1
    await task2
    await task3


asyncio.run(start_tournament())
