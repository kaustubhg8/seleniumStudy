"""Logging"""
import logging

logging.basicConfig(filename="D://scrap//seleniumScreenshots//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")

logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")