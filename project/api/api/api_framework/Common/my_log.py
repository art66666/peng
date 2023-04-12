import logging
from api.api_framework.Common.project_path import *


class MyLog:
    def my_log(self,msg,level):
        # 定义一个日志收集器 my_logger
        my_logger=logging.getLogger('1.txt')
        # 设定级别setLevel
        my_logger.setLevel('DEBUG')
        # 设置日志输出格式logging.Formatter
        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-日志信息:%(message)s')
        # 创建一个我们自己的输出渠道
        # 控制台输出logging.StreamHandler
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)
        # 输出到指定文件logging.FileHandler
        fh = logging.FileHandler(my_log_path,encoding='UTF-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)
        # 两者对接，指定输入渠道:收集器.addHandler(输出渠道)
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        # 收集日志
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)
        # 关闭日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')
    def info(self,msg):
        self.my_log(msg,'INFO')
    def warning(self,msg):
        self.my_log(msg,'WARNING')
    def error(self,msg):
        self.my_log(msg,'ERROR')
    def critical(self,msg):
        self.my_log(msg,'CRITICAL')


