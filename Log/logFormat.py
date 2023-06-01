import logging

logging.basicConfig(filename= "LogFolder\\logb.log", format= '%(asctime)s: %(message)s: %(levelname)s' ,level= logging.DEBUG)
# format %(anything)s -> It 'll convert anything to string
# asctime -> fetch the current system time in global format, message - passed on logging level.
# level -> Basically from warning. If basic log is required then mention, "level= logging.DEBUG". It will display all the logs.

logging.debug("Am a debug log")
logging.info("Am a info log")
logging.warning("Am a warning log")
logging.error("Am a error log")
logging.critical("Am a critical log")

