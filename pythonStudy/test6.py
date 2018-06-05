import os, time, random
from multiprocessing import Process, Queue
from multiprocessing import Pool
import time, threading


print('Process (%s) start' % os.getpid())

# pid = os.fork()
pid = 0
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    
def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))

def TestProcess():
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test', ))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(p):
    print('Process to read: %s' % os.getpid())
    while True:
        value = p.get(True)
        print('Get %s from queue...' % value)

def ReadWrite():
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def TestThreading():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s is ended.' % threading.current_thread().name)


balance = 0
lock = threading.Lock()
local_school = threading.local()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

def TestMutilThread():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

def TestThreadLocal():
    t1 = threading.Thread(target=process_thread, args=('SLY',))
    t2 = threading.Thread(target=process_thread, args=('Huang',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()



if __name__ == '__main__':
    # TestProcess()
    # ReadWrite()
    # TestThreading()
    # TestMutilThread()
    TestThreadLocal()


