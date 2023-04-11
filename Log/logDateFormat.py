import logging

logging.basicConfig(filename= "LogFolder\\logc.log", format= '%(asctime)s: %(levelname)s: %(message)s' , datefmt= '%d/%m/%Y %I:%M:%S %p' , level= logging.DEBUG)
# dateformat = %d/%m/%Y %I:%M:%S %p -> date,month,year Indiantime,Minutes,Seconds meridian

logging.debug("Am a debug log")
logging.info("Am a info log")
logging.warning("Am a warning log")
logging.error("Am a error log")
logging.critical("Am a critical log")

