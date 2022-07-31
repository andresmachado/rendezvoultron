from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import config
import logger


# Globals
driver = None
logger = logger.instance


def init(p_logger):
    global logger
    logger = p_logger


def start(headless=False):
    global driver

    if not headless:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif config.headless:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.binary_location = config.chrome_bin
        driver = webdriver.Chrome(
            executable_path=config.chrome_driver_bin,
            chrome_options=chrome_options
        )
    else:
        driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    logger.info('Selenium started')
