import os

from dotenv import load_dotenv

import logger

logger = logger.instance

chrome_driver_bin = "/usr/local/bin/chromedriver"
chrome_bin = None

env_path = os.path.dirname(os.path.realpath(__file__)) + '/.env'
load_dotenv(dotenv_path=env_path)

headless = os.getenv('HEADLESS', 'true') == 'true'


def init_web():
    """Initialize environment variables in preparation for web interaction."""
    global chrome_driver_bin
    global chrome_bin

    chrome_driver_bin = os.getenv('CHROME_DRIVER_BIN')
    chrome_bin = os.getenv('CHROME_BIN')
