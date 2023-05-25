import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import config
import logger
import web

# Globals
from utils import PersonLoader

logger = logger.instance
URL = "https://rvsq.gouv.qc.ca/prendrerendezvous/"


def main():
    logger.info("Script started.")
    config.init_web()

    web.start()
    driver = web.driver
    driver.get(URL)

    person = PersonLoader().get_person()

    first_name = driver.find_element(
        By.NAME, "ctl00$ContentPlaceHolderMP$AssureForm_FirstName"
    )
    first_name.send_keys(person.first_name)

    last_name = driver.find_element(
        By.NAME, "ctl00$ContentPlaceHolderMP$AssureForm_LastName"
    )
    last_name.send_keys(person.last_name)

    ramq = driver.find_element(By.NAME, "ctl00$ContentPlaceHolderMP$AssureForm_NAM")
    ramq.send_keys(person.ramq)

    ramq_seq = driver.find_element(
        By.NAME, "ctl00$ContentPlaceHolderMP$AssureForm_CardSeqNumber"
    )
    ramq_seq.send_keys(person.ramq_seq)

    dob_day = driver.find_element(By.NAME, "ctl00$ContentPlaceHolderMP$AssureForm_Day")
    dob_day.send_keys(person.dob_day)

    dob_month = Select(
        driver.find_element(By.NAME, "ctl00$ContentPlaceHolderMP$AssureForm_Month")
    )
    dob_month.select_by_value(person.dob_month)

    dob_year = driver.find_element(
        By.NAME, "ctl00$ContentPlaceHolderMP$AssureForm_Year"
    )
    dob_year.send_keys(person.dob_year)

    genre = driver.find_element(By.ID, "ctl00_ContentPlaceHolderMP_MaleGender")
    if person.genre == "F":
        genre = driver.find_element(By.ID, "ctl00_ContentPlaceHolderMP_FemaleGender")
    genre.click()

    submit_btn = driver.find_element(By.NAME, "ctl00$ContentPlaceHolderMP$myButton")
    submit_btn.click()

    WebDriverWait(driver, 3).until(
        EC.invisibility_of_element_located((By.ID, "greyCover"))
    )

    try:
        btn_pop_up = driver.find_element(By.CLASS_NAME, "modal-dialog").find_element(
            By.CSS_SELECTOR, "button"
        )
        btn_pop_up.click()
    except Exception as e:
        logger.warning(e)

    next_step_link = driver.find_element(
        By.XPATH, "//div[text()='Prendre rendez-vous dans une clinique à proximité']"
    )
    next_step_link.click()

    # date_range = driver.find_element(By.ID, "DateRangeStart")
    # date_range.clear()
    # date_range.click()
    # date_range.send_keys(person.date_range)

    consulting_reason = Select(driver.find_element(By.NAME, "consultingReason"))
    consulting_reason.select_by_value(person.reason)

    perimeter = Select(driver.find_element(By.NAME, "perimeterCombo"))
    perimeter.select_by_value(person.perimeter)

    search_btn = driver.find_element(By.XPATH, "//button[text()='Rechercher']")

    search_btn.click()

    # clinicsWithNoDisponibilitiesContainer
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.ID, "clinicsWithNoDisponibilitiesContainer")
        )
    )

    no_available_clinics = True

    while no_available_clinics:
        try:
            search_btn.click()
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located(
                    (By.ID, "clinicsWithNoDisponibilitiesContainer")
                )
            )
            no_available_clinics = driver.find_element(
                By.ID, "clinicsWithNoDisponibilitiesContainer"
            )
        except ElementClickInterceptedException:
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located(
                    (By.ID, "clinicsWithNoDisponibilitiesContainer")
                )
            )
            no_available_clinics = driver.find_element(
                By.ID, "clinicsWithNoDisponibilitiesContainer"
            )

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "ClinicList"))
    )

    clinic_list = driver.find_elements_by_class_name("h-selectClinic")
    first_clinic = clinic_list[1]
    first_clinic.click()


if __name__ == "__main__":
    main()
