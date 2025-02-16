from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.insider_locators import InsiderLocators
import time

class CareersPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def verify_life_at_insider(self):
        life_at_insider = self.wait.until(
            EC.presence_of_element_located(InsiderLocators.LIFE_AT_INSIDER)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", life_at_insider)
        assert life_at_insider.is_displayed()
        time.sleep(2)
        return self

    def verify_locations(self):
        locations = self.wait.until(
            EC.presence_of_element_located(InsiderLocators.LOCATIONS)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", locations)
        assert locations.is_displayed()
        time.sleep(2)
        return self

    def check_teams_section(self):
        teams_section = self.wait.until(
            EC.presence_of_element_located(InsiderLocators.TEAMS_SECTION)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", teams_section)
        time.sleep(2)
        return self

    def click_see_all_teams(self):
        see_all_teams = self.wait.until(
            EC.element_to_be_clickable(InsiderLocators.SEE_ALL_TEAMS)
        )
        # Elementi görünür hale getir
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", see_all_teams)
        time.sleep(2)  # Scroll animasyonunun tamamlanmasını bekle
        
        # ActionChains ile tıklama
        self.actions.move_to_element(see_all_teams).pause(1).click().perform()
        
        time.sleep(2)
        return self

    def verify_team_items(self):
        teams_content = self.wait.until(
            EC.presence_of_all_elements_located(InsiderLocators.TEAM_ITEMS)
        )
        for item in teams_content:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", item)
            assert item.is_displayed()
            time.sleep(1)
        return self

    def click_find_your_dream_job(self):
        dream_job_button = self.wait.until(
            EC.element_to_be_clickable(InsiderLocators.DREAM_JOB_BUTTON)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", dream_job_button)
        time.sleep(2)
        dream_job_button.click()
        time.sleep(7)  
        return self 