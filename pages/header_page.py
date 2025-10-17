from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    def check_header(self):
        return self.find_element_with_wait(HeaderPageLocators.HEADER) and self.find_element_with_wait(HeaderPageLocators.LOGO) and self.find_element_with_wait(HeaderPageLocators.PROJECTS) and self.find_element_with_wait(HeaderPageLocators.MENU)
