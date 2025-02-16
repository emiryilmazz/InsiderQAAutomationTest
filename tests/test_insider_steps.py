from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.positions_page import PositionsPage

class TestInsiderWebsite:
    @pytest.fixture
    def browser(self):
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        
        service = Service()
        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
        yield driver
        driver.quit()

    def test_insider_website(self, browser):
        # Ana sayfa işlemleri
        home_page = HomePage(browser)
        home_page.navigate_to()
        home_page.reject_cookies()
        home_page.verify_logo()
        home_page.click_company()
        home_page.click_careers()

        # Careers sayfası işlemleri
        careers_page = CareersPage(browser)
        careers_page.verify_life_at_insider()
        careers_page.verify_locations()
        careers_page.check_teams_section()
        careers_page.click_see_all_teams()
        careers_page.verify_team_items()
        careers_page.click_find_your_dream_job()

        # Açık pozisyonlar sayfası işlemleri
        positions_page = PositionsPage(browser)
        positions_page.select_department()
        positions_page.select_location()
        positions_page.take_jobs_screenshot()
        positions_page.select_random_job()
        positions_page.switch_to_application_form() 