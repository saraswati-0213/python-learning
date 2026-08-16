# import time
# def task1():
#     print("task 1 started")
#     time.sleep(2)
#     print("task 1 completed")
# def task2():
#     print("task 2 stared")
#     time.sleep(2)
#     print("task2 compleed")
# print(task1())
# print(task2()) this is synchronous programming
import asyncio
import time
# async def greet():
#     print("hello")
# asyncio.run(greet())
async def greet():
    print("start")
    time.sleep(5)
    print("end")
asyncio.run(greet())