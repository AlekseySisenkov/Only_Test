from selenium.webdriver.common.by import By

class HeaderPageLocators:
    HEADER = By.XPATH, '//header'
    LOGO = By.CLASS_NAME, 'Header_logo__eoAf_'
    PROJECTS = By.XPATH, '//a[@href="/projects"]'
    MENU = By.XPATH, '//a[@href="/company"]'