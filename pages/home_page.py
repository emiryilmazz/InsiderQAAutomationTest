from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.insider_locators import InsiderLocators
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self):
        self.driver.get("https://useinsider.com/")
        return self

    def reject_cookies(self):
        try:
            reject_button = self.wait.until(
                EC.element_to_be_clickable(InsiderLocators.REJECT_COOKIES)
            )
            reject_button.click()
        except:
            print("Cookie bildirimi bulunamadı veya zaten reddedildi")
        return self

    def verify_logo(self):
        logo = self.wait.until(
            EC.presence_of_element_located(InsiderLocators.LOGO)
        )
        assert logo.is_displayed()
        assert "Insider" in self.driver.title
        return self

    def click_company(self):
        company_button = self.wait.until(
            EC.element_to_be_clickable(InsiderLocators.COMPANY_BUTTON)
        )
        company_button.click()
        time.sleep(3)
        return self

    def click_careers(self):
        careers_link = self.wait.until(
            EC.element_to_be_clickable(InsiderLocators.CAREERS_LINK)
        )
        careers_link.click()
        return self 