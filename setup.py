# @Time         : 18-2-13 下午9:06
# @Author       : DioMryang
# @File         : setup.py
# @Description  :
from setuptools import setup, find_packages
from DioScheduler import __version__

setup(
    name="DioScheduler",
    version=__version__,
    description="dio 调度程序",
    author="dio_mryang",
    url="https://github.com/YangXiaos/",
    packages=find_packages(), install_requires=[]
)
