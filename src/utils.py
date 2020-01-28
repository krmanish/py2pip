import config


SHOW_PRINT = config.SHOW_PRINT


class Logger(object):

    def __init__(self, show_print=False):
        self.show_print = show_print

    def info(self, msg):
        if SHOW_PRINT or self.show_print:
            print(msg)

    def error(self, msg):
        if SHOW_PRINT or self.show_print:
            print(msg)