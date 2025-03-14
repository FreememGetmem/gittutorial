import logging

## Configuring logging
logging.basicConfig(
    filename='apps.log',
    filemode='a',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:M:%S'
    )
## Log messages
#logging.debug("This is a debug message")
#logging.info("This is an info message")
#logging.warning("This is a warning message")
#logging.error("this is an error message")
#logging.critical("this is a critical message")