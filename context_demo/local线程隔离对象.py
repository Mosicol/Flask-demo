# from threading import Thread

# request = '123'
#
# class MyThread(Thread):
#     def run(self):
#         global request
#         request = 'abc'
#         print('子线程',request)   #子线程 abc
#
# mythread = MyThread()
# mythread.start()
# mythread.join()
#
# print('主线程',request)          #主线程 abc


# ==========================local对象：在每个线程中都是隔离的====================

from threading import Thread
from werkzeug.local import Local

#只要绑定在Local对象上的属性，在每个线程中都是隔离的
locals = Local()
locals.request = '123'

class MyThread(Thread):
    def run(self):
        locals.request = 'abc'
        print('子线程',locals.request)   #子线程 abc

mythread = MyThread()
mythread.start()
mythread.join()

print('主线程',locals.request)          #主线程 123



