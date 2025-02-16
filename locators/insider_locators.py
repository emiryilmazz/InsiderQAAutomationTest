from selenium.webdriver.common.by import By

class InsiderLocators:
    # Ana Sayfa Locator'ları
    LOGO = (By.CSS_SELECTOR, "a.navbar-brand")
    COMPANY_BUTTON = (By.XPATH, "//div[@id='navbarNavDropdown']/ul[@class='navbar-nav']/li[6]/a[@id='navbarDropdownMenuLink']")
    CAREERS_LINK = (By.XPATH, "/html//div[@id='navbarNavDropdown']/ul[@class='navbar-nav']//a[@href='https://useinsider.com/careers/']")
    REJECT_COOKIES = (By.ID, "wt-cli-reject-btn")

    # Careers Sayfası Locator'ları
    LIFE_AT_INSIDER = (By.XPATH, "//body/div[@class='elementor elementor-22610']/section[4]//div[@class='elementor-element elementor-element-21cea83 elementor-widget elementor-widget-heading']//h2[@class='elementor-heading-title elementor-size-default']")
    LOCATIONS = (By.XPATH, "/html//section[@id='career-our-location']/div[@class='container']//h3[@class='category-title-media ml-0']")
    TEAMS_SECTION = (By.ID, "career-find-our-calling")
    SEE_ALL_TEAMS = (By.CSS_SELECTOR, "a.btn.btn-outline-secondary.rounded.text-medium.mt-5.mx-auto.py-3.loadmore")
    TEAM_ITEMS = (By.CSS_SELECTOR, "#career-find-our-calling .job-item")
    DREAM_JOB_BUTTON = (By.XPATH, "/html//section[@id='page-head']/div[@class='container']//a[@href='https://useinsider.com/open-positions/']")

    # Açık Pozisyonlar Sayfası Locator'ları
    DEPARTMENT_DROPDOWN = (By.CSS_SELECTOR, "span#select2-filter-by-department-container")
    LOCATION_DROPDOWN = (By.CSS_SELECTOR, "span#select2-filter-by-location-container")
    DROPDOWN_OPTIONS = (By.CLASS_NAME, "select2-results__options")
    QA_OPTION = (By.XPATH, "//li[contains(@class, 'select2-results__option') and contains(text(), 'Quality Assurance')]")
    LOCATION_OPTIONS = (By.CSS_SELECTOR, "li.select2-results__option")
    POSITION_LIST = (By.CSS_SELECTOR, ".position-list")
    JOB_CARDS = (By.CSS_SELECTOR, ".position-list .position-list-item")
    VIEW_ROLE_BUTTON = (By.CSS_SELECTOR, "a[href*='lever']") 