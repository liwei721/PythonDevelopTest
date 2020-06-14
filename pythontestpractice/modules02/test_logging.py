"""
    @author: xuanke
    @time: 2020/6/9
    @function: 对日志模块logging进行验证
"""
import logging
import pythontestpractice.config as config


class LoggerUtil(logging.Logger):
    """
     初始化方法中参数：
     @name： 获取Logger传入的值，多次调用保持一致即可
     @level： 默认的日志级别是DEBUG。
     @file： 日志文件名称，默认是空
     @format： 表示对日志格式化的默认格式。
    """

    def __init__(self, name="loggerUtil", stream_level=logging.DEBUG, file_level=logging.ERROR, file=None,
                 format="%(filename)s:%(lineno)d:%(name)s:%(levelname)s:%(message)s"):
        # 初始化日志收集器，调用父类的__init__可以直接使用父类的打印日志方法：debug()、info()等。
        super().__init__(name, stream_level)
        # logger = logging.getLogger(name)
        # 日志开关是全局配置
        if not config.is_log:
            self.addHandler(logging.NullHandler())
            return
        # 设置日志的级别
        self.setLevel(stream_level)
        # 初始化format，设置格式
        fmt = logging.Formatter(format)
        # 初始化处理器
        # 如果file为空，就只将日志输出到控制台。如果file不为空，则内容同时输出到文件和控制台。
        if file:
            file_handler = logging.FileHandler(file)
            # 设置handler级别
            file_handler.setLevel(file_level)
            # 添加handler
            self.addHandler(file_handler)
            # 添加日志处理器
            file_handler.setFormatter(fmt)

        def filter_password(record):
            """
            对日志进行过滤，不打印password
            :param record:
            :return:
            """
            print(record)
            if "password" in record.msg:
                return False
            return True
        logging_password = logging.Filter()
        logging_password.filter = filter_password
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(stream_level)
        # stream_handler.addFilter(logging_password)
        self.addHandler(stream_handler)
        self.addFilter(logging_password)
        stream_handler.setFormatter(fmt)


if __name__ == '__main__':
    my_logger = LoggerUtil()
    my_logger.debug("test info")
    my_logger.error("test error")
    my_logger.critical("test critical")
    my_logger.critical("password test critical")
