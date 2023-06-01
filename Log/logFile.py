import logging

logging.basicConfig(filename= "LogFolder\\loga.log", level= logging.DEBUG) # storing log into a file -> folder name followed by file name(Auto creation)
# "level= logging.DEBUG" level debug means all level will be executed though it's a basic(Debug, Info) level.

logging.debug("Am a debug log")
logging.info("Am a info log")
logging.warning("Am a warning log")
logging.error("Am a error log")
logging.critical("Am a critical log")

