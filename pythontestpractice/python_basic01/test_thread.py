"""
    @author: xuanke
    @time: 2020/5/12
    @function: 对多线程和多进程进行验证
"""
import threading
import time

def direct_run(thread_name):
    print("running thread: %s" % thread_name)


def test_direct_thread():
    """
    验证直接调用threading的方式
    :return:
    """
    t1 = threading.Thread(target=direct_run, args=("first",))
    t2 = threading.Thread(target=direct_run, args=("second",))
    t1.start()
    t2.start()


class MyThread(threading.Thread):
    def __init__(self, thread_name):
        super(MyThread, self).__init__()
        self.thread_name = thread_name

    def run(self):
        print("run thread %s" % self.thread_name)


def cost_run(thread_name):
    print("running thread: %s" % thread_name)
    time.sleep(20)
    print("%s thread exec finished" % thread_name)


if __name__ == '__main__':
    # t1 = MyThread("first")
    # t2 = MyThread("second")
    # t1.start()
    # t2.start()

    for i in range(10):
        t = threading.Thread(target=cost_run, args=('thread%d' % i,))
        t.setDaemon(True)
        t.start()
    print('all exec finished')

