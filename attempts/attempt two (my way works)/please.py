import test
import logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
test.logger.info('Testing, testing, one, two, three')