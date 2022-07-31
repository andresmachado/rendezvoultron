import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import config
import web
import logger

# Globals
from utils import PersonLoader

logger = logger.instance
URL = "https://rvsq.gouv.qc.ca/prendrerendezvous/"


def main():
    logger.info('Script started.')
    config.init_web()

    web.start()
    driver = web.driver
    driver.get(URL)

    person = PersonLoader().get_person()

    first_name = driver.find_element_by_name("ctl00$ContentPlaceHolderMP$AssureForm_FirstName")
    first_name.send_keys(person.first_name)

    last_name = driver.find_element_by_name("ctl00$ContentPlaceHolderMP$AssureForm_LastName")
    last_name.send_keys(person.last_name)

    ramq = driver.find_element_by_name("ctl00$ContentPlaceHolderMP$AssureForm_NAM")
    ramq.send_keys(person.ramq)

    ramq_seq = driver.find_element_by_name("ctl00$ContentPlaceHolderMP$AssureForm_CardSeqNumber")
    ramq_seq.send_keys(person.ramq_seq)

    dob_day = driver.find_element_by_name("ctl00$ContentPlaceHolderMP$AssureForm_Day")
    dob_day.send_keys(person.dob_day)

    dob_month = Select(driver.find_element_by_name("ctl00$ContentPlaceHolderMP$AssureForm_Month"))
    dob_month.select_by_value(person.dob_month)

    dob_year = driver.find_element_by_name("ctl00$ContentPlaceHolderMP$AssureForm_Year")
    dob_year.send_keys(person.dob_year)

    genre = driver.find_element_by_name("ctl00$ContentPlaceHolderMP$FemaleOrMale")
    genre.click()

    submit_btn = driver.find_element_by_name("ctl00$ContentPlaceHolderMP$myButton")
    submit_btn.click()

    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.ID, "greyCover")))

    next_step_link = driver.find_element_by_xpath(
        "//div[text()='Prendre rendez-vous dans une clinique à proximité']"
    )
    next_step_link.click()

    date_range = driver.find_element_by_id("DateRangeStart")
    date_range.clear()
    date_range.click()
    date_range.send_keys(person.date_range)

    consulting_reason = Select(driver.find_element_by_name("consultingReason"))
    consulting_reason.select_by_value("38663537-3261-3233-2d31-3033352d3431")

    perimeter = Select(driver.find_element_by_name("perimeterCombo"))
    perimeter.select_by_value("1")

    search_btn = driver.find_element_by_xpath(
        "//button[text()='Rechercher']"
    )

    search_btn.click()

    # clinicsWithNoDisponibilitiesContainer
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "clinicsWithNoDisponibilitiesContainer"))
    )

    no_available_clinics = True

    while no_available_clinics:
        try:
            search_btn.click()
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "clinicsWithNoDisponibilitiesContainer"))
            )
            no_available_clinics = driver.find_element_by_id(
                "clinicsWithNoDisponibilitiesContainer"
            )
        except ElementClickInterceptedException:
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "clinicsWithNoDisponibilitiesContainer"))
            )
            no_available_clinics = driver.find_element_by_id(
                "clinicsWithNoDisponibilitiesContainer"
            )


if __name__ == '__main__':
    main()
