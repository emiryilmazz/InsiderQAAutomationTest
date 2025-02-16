from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.insider_locators import InsiderLocators
import time
import random
import os
from datetime import datetime

class PositionsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def select_department(self, department="Quality Assurance"):
        # Sayfanın yüklenmesi için bekle
        time.sleep(5)
        
        department_dropdown = self.wait.until(
            EC.element_to_be_clickable(InsiderLocators.DEPARTMENT_DROPDOWN)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", department_dropdown)
        time.sleep(3)
        department_dropdown.click()
        time.sleep(3)

        dropdown_menu = self.wait.until(
            EC.presence_of_element_located(InsiderLocators.DROPDOWN_OPTIONS)
        )
        time.sleep(2)

        qa_options = self.driver.find_elements(*InsiderLocators.QA_OPTION)
        if len(qa_options) > 0:
            qa_options[0].click()
        else:
            raise Exception(f"{department} seçeneği bulunamadı!")
        time.sleep(3)
        return self

    def select_location(self, location_index=1):  # 1 = Istanbul
        location_dropdown = self.wait.until(
            EC.element_to_be_clickable(InsiderLocators.LOCATION_DROPDOWN)
        )
        location_dropdown.click()
        time.sleep(2)

        location_options = self.wait.until(
            EC.presence_of_all_elements_located(InsiderLocators.LOCATION_OPTIONS)
        )

        print("\nMevcut lokasyon seçenekleri:")
        for i, option in enumerate(location_options):
            print(f"{i}: {option.text}")

        location_options[location_index].click()
        time.sleep(2)
        return self

    def take_jobs_screenshot(self):
        jobs_section = self.wait.until(
            EC.presence_of_element_located(InsiderLocators.POSITION_LIST)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", jobs_section)
        time.sleep(2)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join("Screenshots", f"filtered_jobs_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Filtrelenmiş iş ilanlarının ekran görüntüsü '{screenshot_path}' olarak kaydedildi.")
        return self

    def select_random_job(self):
        job_cards = self.wait.until(
            EC.presence_of_all_elements_located(InsiderLocators.JOB_CARDS)
        )

        if not job_cards:
            raise Exception("Hiç iş ilanı bulunamadı!")

        random_job = random.choice(job_cards)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", random_job)
        time.sleep(2)

        ActionChains(self.driver).move_to_element(random_job).perform()
        time.sleep(2)

        view_role_button = random_job.find_element(*InsiderLocators.VIEW_ROLE_BUTTON)
        view_role_button.click()
        time.sleep(3)
        return self

    def switch_to_application_form(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)

        current_url = self.driver.current_url
        assert "lever" in current_url.lower(), "Lever başvuru formuna yönlendirilmedi!"
        print(f"Başvuru formu URL'si: {current_url}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join("Screenshots", f"application_form_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Başvuru formunun ekran görüntüsü '{screenshot_path}' olarak kaydedildi.")
        return self 