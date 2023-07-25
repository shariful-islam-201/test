import logging

class LoggerD():
    def sample_log(self):
        logger =  logging.getLogger("demologger")
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')

        ch = logging.StreamHandler()  ## ch is used for console logging
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        fh = logging.FileHandler("logs/demo.log")  ## fh is used for file logging
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.debug("Debug Log Message")
        logger.info("Debug Log Message")
        logger.warning("Debug Log Message")
        logger.critical("Debug Log Message")
        logger.error("Debug Log Message")




ld = LoggerD()
ld.sample_log()

