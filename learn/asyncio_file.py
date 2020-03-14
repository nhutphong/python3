
import time
import asyncio
import threading


async def find_div(inrange, div_by):
    print(f"start num range({inrange}) / {div_by}")
    located = []

    for i in range(inrange):
            if i % div_by == 0:
                located.append(i)
            elif i % 500000 == 0:
               await asyncio.sleep(.0001)

    print(f"done range({inrange}) / {div_by}")
    return located


async def main():
    await asyncio.wait([find_div(1008000, 350),
                        find_div(2000800, 2000),
                        find_div(350, 30)
                ])


async def say(what, when):
    await asyncio.sleep(when)
    print(what)


async def mot(stop=100):
    print("Tao la 1111111")

    for i in range(stop):
        if i == 5:
            await asyncio.sleep(4)

    print('end 111111111')
    return 'mot()'

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


async def hello(name='one', label='-',delay=.25):
    print(f"{name:}")

    for i in range(21):
        print(f"{name:{label}<{i}} {i}")
        await asyncio.sleep(delay)


def asyncio_main():
    begin = time.time()

    loop = asyncio.get_event_loop()

    tasks = [asyncio.ensure_future(hello()), asyncio.ensure_future(hello('TWO','#', 1))]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    print(f"microsecond : {end-begin}")
    # loop.run_forever()

COUNT = 0
async def print_flush_true(text='phong',* , delay=.1):
    global COUNT
    COUNT+=1
    print(f"thread = {COUNT:.>20}")
    # flush=True => in tu tren xuong cho sleep xong roi in tiep
    # flush=Flase => cho sleep xong roi moi in 1 luc tat ca
    for c in text:
        print(c, end='', flush=True)
        await asyncio.sleep(delay)

    print()

async def print_async(text='phong',* , count=2, delay=.1):
    tasks = []
    for _ in range(count):
        task = asyncio.create_task(print_flush_true(text, delay=delay))
        tasks.append(task)

    print(f"started at {time.strftime('%X')}") # '%X' => hh:mm:ss, '%x' => m/d/y
    await asyncio.wait(tasks)
    print(f"finished at {time.strftime('%X')}")

#one create function coro
async def say_after(delay, what):
    print(f"START {what} {delay:.>10}")
    await asyncio.sleep(delay)
    print(f"END {what:.>10}", end='\n'*2)

# python 3.7
async def say_after_main():
    """ code run tu tren xuong, khi gap await thi quay len treb chay theo cac create_task() tu tren xuong duoi"""


    print(f"started at {time.strftime('%X')}")

    #two create tasks -> dung asyncio.gather, .wait co the bo buoc #two
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

    # await asyncio.wait([say_after(9,'9'), say_after(7,'7'), say_after(3,'3')],) # run coro() co time bé nhất
    #three
    await asyncio.gather(say_after(9,'9'), say_after(3,'3'), say_after(7,'7'),)

    print(f"finished at {time.strftime('%X')}")
# python 3.7

# asyncio.run(say_after_main()) #three


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

if __name__ == '__main__':
    pass
