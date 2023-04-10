import logging

logging.basicConfig(format ='%(asctime)s %(message)s', filename='logs_file.log')
logging = logging.getLogger()
# this is happening in background in sepearte thread so not using program complile memory and doesn't affect code
#so it is better to use in python program

logging.info("this is fine")
logging.warning("this may break")
logging.error("fix this error")
logging.critical("This is really critical error solve asap")
