
import time
import asyncio
import threading
#-----------------------------------------------------------------------------#
#nen dung tu python3.8 syntax don gian
async def numbers(number):
    total = 0
    for num in range(1, number+1):
        await asyncio.sleep(.25)
        print(f"{num} ", end='', flush=True)
        total += num

    return total


async def alphabets(chars):
    for char in chars:
        await asyncio.sleep(.4)
        print(f"{char} ", end='', flush=True)

    return chars[::-1]


async def run_async():
    print(f"{'run_async END':-^85}")
    # asyncio.gather(*coros) => *coros = so luong coros chinh
    """ 
    neu co 4 func trong gather(*coros)  thi co 4 coros chinh
    se run tuan tu 4 coros truoc, sau do neu gap asyncio.sleep() thu 5 se chuyen toi coro truoc do, co asyncio.sleep() co thoi gian it nhat run tiep
    """
    number, alphabet = await asyncio.gather(numbers(5), alphabets('phong'))

    print(f"\nnumbers: {number} - alphabets: {alphabet}")

    print(f"\n{'run_async START':-^85}")
    return [number, alphabet]

asyncio.run(run_async())
#-----------------------------------------------------------------------------#

async def say_after(delay, what):
    print(f"START {what} {delay:.>10}")
    await asyncio.sleep(delay)
    print(f"END {what:.>10}", end='\n'*2)

# python 3.7
async def say_after_main():
    """ code run tu tren xuong, khi gap await thi quay len treb chay theo cac create_task() tu tren xuong duoi"""


    print(f"started at {time.strftime('%X')}")

    #two create tasks -> dung asyncio.gather co the bo buoc #two
    # task1 = asyncio.create_task(say_after(5,'5'))
    # task2 = asyncio.create_task(say_after(3,'3'))
    # task4 = asyncio.create_task(say_after(7,'7'))
    # task3 = asyncio.create_task(say_after(1,'1'))
    """ await chờ task2 ket thuc rồi chạy het chuong trinh, cac task co thoi gian lau hon se bo qua
     """
    # await cho_5p => t chờ tui bay 5p, het 5p t chay het func cua tao
    # await tasks = run asyncio.create_task(fun())
    # await task1
    # await task2
    # await task4

    #three
    await asyncio.gather(say_after(9,'9'), say_after(3,'3'), say_after(7,'7'),)

    print(f"finished at {time.strftime('%X')}")
# python 3.8
# asyncio.run(say_after_main()) #three


#=============================================================================#


# python 3.6 va cu hon
def say_after_until():
    """ goi ten ham say_after_until() khong can asyncio.run(say_after_until())"""


    print(f"started at {time.strftime('%X')}")

    loop = asyncio.get_event_loop()

    task1 = loop.create_task(say_after(5,'5'))
    task2 = loop.create_task(say_after(3,'3'))
    task3 = loop.create_task(say_after(7,'7'))
    task4 = loop.create_task(say_after(1,'1'))
    loop.run_until_complete(asyncio.gather(task2))
    # loop.run_until_complete(asyncio.gather(task1, task4, task3, task2))
    # run theo luc loop.create_task, chu ko phai theo asyncio.gather(*task)

    print(f"finished at {time.strftime('%X')}")
# say_after_until()
#=============================================================================#


def thread_test(name='one',label='#', stop=30, delay=1):
    print(f"{name} let go!!!")

    for i in range(stop):
        print(f'{name}: {i:{label}>20}')
        time.sleep(delay)

def thread_main():

    r1 = threading.Thread(target=thread_test, args=('one','#',16,4))
    r2 = threading.Thread(target=thread_test, args=('two','-',40,1))

    r2.start()
    r1.start()

    threads = [r1, r2]
    for r in threads:
        r.join()

    print('end threading')
    

if __name__ == '__main__':
    pass