# coding=utf-8
from multiprocessing.pool import ThreadPool
import time
import os
import psutil
import json
import threadpool
import threading


class TEST(object):
    # 获取数据，使用yield, 每次返回一个len=10的list, list中的每一项是一个线程的数据
    def get_data(self):
        multi_list = list()
        for i in range(100):
            data = "abcdefg" * 100000
            multi_list.append(data)
            if len(multi_list) % 10 == 0:
                yield multi_list
                multi_list = list()

    # 测试函数
    def test(self):
        for data in self.get_data():
            mem = psutil.Process(os.getpid()).memory_info().rss
            print("[test] mem %s" % mem)    # 打印内存占用情况
            self.deal_multi_thread(data)      # 使用threadpool
            # self.deal_multi_thread(data)  # 使用threading

    # 待对比方法，threadpool
    def deal_threadpool(self, data_list):
        pool = threadpool.ThreadPool(10)
        requests = threadpool.makeRequests(self.sub_task, data_list)
        [pool.putRequest(req) for req in requests]
        pool.wait()

    # 待对比方法，threading
    def deal_multi_thread(self, data_list):
        threads = list()
        for data in data_list:
            threads.append(threading.Thread(target=self.sub_task, args=(data,)))
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    def sub_task(self, data):
        return


if __name__ == "__main__":
    mem = psutil.Process(os.getpid()).memory_info().rss
    print("[main] mem %s" % mem)
    obj = TEST()
    obj.test()
    mem = psutil.Process(os.getpid()).memory_info().rss
    print("[main] mem %s" % mem)