import os
import logging
import logging.handlers


class MyLogger:
    def __init__(self, logname, logdir):
        self.initLogDir(logdir)
        self.setDefaultLogger(logname, logdir)

    def initLogDir(self, logdir):
        if not os.path.exists(logdir):
            os.makedirs(logdir)

    def setDefaultLogger(self, logname, logdir):
        self.logger = logging.getLogger(logname)
        self.setFormatter(
            '[%(asctime)s][%(processName)-10s][%(levelname)s] - %(message)s')
        self.setLevel('INFO')
        self.setFileHandler(f'{logname}.log', logdir)
        self.setStreamHandler()
        # self.setTimeHandler(f'{logname}.log', logdir)

    def setFormatter(self, fmt):
        self.formatter = logging.Formatter(fmt)

    def setLevel(self, level):
        level = level.upper()
        cases = {
            'DEBUG': lambda: self.logger.setLevel(logging.DEBUG),
            'INFO': lambda: self.logger.setLevel(logging.INFO),
            'WARNING': lambda: self.logger.setLevel(logging.WARNING),
            'ERROR': lambda: self.logger.setLevel(logging.ERROR),
        }
        cases.get(level, lambda: self.logger.setLevel(logging.INFO))()

    def setFileHandler(self, logname, logdir, fileMaxByte=1024*1024*2, backupCount=5):
        fileHandler = logging.handlers.RotatingFileHandler(
            f'{logdir}/{logname}', maxBytes=fileMaxByte, backupCount=backupCount)
        fileHandler.setFormatter(self.formatter)
        self.logger.addHandler(fileHandler)

    def setStreamHandler(self):
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(self.formatter)
        self.logger.addHandler(streamHandler)

    def setTimeHandler(self, logname, logdir, when="midnight", interval=1):
        timeHandler = logging.TimedRotatingFileHandler(
            f'{logdir}/{logname}', when, interval)
        timeHandler.suffix = "%Y%m%d"
        timeHandler.setFormatter(self.formatter)
        self.logger.addHandler(timeHandler)

    def getLogger(self):
        return self.logger


if __name__ == '__main__':
    mylogger = MyLogger('mylogger', './log')
    logger = mylogger.getLogger()
    logger.info('test')
