import sys;
import logging;
import logging.handlers
h = logging.StreamHandler()
h.setLevel('DEBUG')
h.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
logger.addHandler(h)
logger.debug('test debug')
logger.info('Test info')
import logging.config
logging.config.dictConfig({"version": 1, "disable_existing_loggers": False})