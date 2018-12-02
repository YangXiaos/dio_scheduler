# @Time         : 18-12-2 下午4:23
# @Author       : DioMryang
# @File         : BossCrawlerScript.py
# @Description  :
import logging

from DioFramework.Base.Job.Job import Job
from DioFramework.Base.Processor.Components.MessageProcessor.MessageWriter import MessageMongodbWriter
from DioSpider.OldSpider.Boss.BossJobSpider import BossJobSpider
from DioSpider.OldSpider.Boss.BossSearchSpider import BossSearchSpider

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    cfg = {
        "id": -1,
        "params": {
            "db_name": "test",
            "collection_name": "boss"
        }
    }
    writer = MessageMongodbWriter(config=cfg)

    enterUrl = "https://www.zhipin.com/c101280100/?query=%E7%88%AC%E8%99%AB&period=3&ka=sel-scale-3"
    job = Job()
    job.id = "boss_crawl_dali"

    result = []
    msgs = BossSearchSpider().crawl(enterUrl, {})

    for msg in msgs:
        writer.run(job, list(BossJobSpider().crawl(msg.getEnterUrl(), {})))
