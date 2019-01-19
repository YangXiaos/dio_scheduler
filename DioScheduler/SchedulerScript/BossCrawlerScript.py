# @Time         : 18-12-2 下午4:23
# @Author       : DioMryang
# @File         : BossCrawlerScript.py
# @Description  :
import logging
import traceback
import time

import schedule
from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Processor.Components.MessageProcessor.MessageWriter import MessageMongodbWriter
from DioSpider.OldSpider.Boss.BossJobSpider import BossJobSpider
from DioSpider.OldSpider.Boss.BossSearchSpider import BossSearchSpider

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] : [%(asctime)s] : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/home/mryang/Project/dio_scheduler/test.log')


# 入口url
ENTER_URL = "https://www.zhipin.com/c101280100/?query=%E7%88%AC%E8%99%AB&period=3&ka=sel-scale-3"


# 跑数函数
def run():
    logging.info("准备跑数")
    writer = MessageMongodbWriter(config={
        "id": -1,
        "params": {
            "db_name": "test",
            "collection_name": "boss"
        }
    })
    job = Job(id="boss_crawl_dali")

    logging.info("搜索爬虫跑数")
    msgs = BossSearchSpider().crawl(ENTER_URL, {})
    logging.info("搜索爬虫跑数 结束")

    for msg in msgs:
        enterUrl = msg.getEnterUrl()
        try:
            logging.info("处理url {}".format(enterUrl))
            rst = list(BossJobSpider().crawl(enterUrl, {}))
            logging.info("写入数据 {}条".format(len(rst)))
            writer.run(job, rst)
            logging.info("写入成功")
        except Exception as e:
            logging.error("{} 跑数失败".format(enterUrl))
            traceback.print_exc()
    logging.info("跑数结束")


def main():
    logging.info("调度程序开始")
    schedule.every(1).hours.do(run)
    run()
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':

    main()
