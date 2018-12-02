# @Time         : 18-12-2 下午3:31
# @Author       : DioMryang
# @File         : __init__.py.py
# @Description  : Scheduler
import typing


class SchedulerV1(object):
    """
    {
        "id": "",

    }
    """

    def __init__(self, id: str, call: typing.Callable):
        self.call = call

    def execute(self):
        """执行调度"""

