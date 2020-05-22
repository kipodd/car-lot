import logging
import logging.handlers

# create hourly rotating log
class Logger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(message)s", datefmt="%d-%m-%y %H:%M:%S"
        )
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename="logs/log", when="h", interval=1, backupCount=24
        )
        console_handler = logging.StreamHandler()

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        file_handler.setFormatter(formatter)

    def add_to_log(self, msg):
        self.logger.info(msg)
