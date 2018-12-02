# @Time         : 18-11-19 下午11:09
# @Author       : DioMryang
# @File         : JobCrawlerScheduler.py
# @Description  :
from threading import Thread

import schedule
import time


def job():
    t = Thread()
    t.start()


schedule.every(10).seconds.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)


