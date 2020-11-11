import logging
import os
import sys

root = os.path.abspath(os.path.dirname(sys.argv[0]))

filename = root + '/logger.log'

logging.basicConfig(filename=filename, level=logging.DEBUG)


def debug(message: str):
    logging.debug(message)
