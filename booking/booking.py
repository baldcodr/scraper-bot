from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
import os

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"usr/local/bin/chromedriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    #close browser
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def open_home_page(self):
        self.get(const.BASE_URL)

    def accept_cookies(self):
        accept_cookies = self.find_element(By.ID,'onetrust-accept-btn-handler')
        accept_cookies.click()

    def select_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        try:
            choose_currency = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"')
            choose_currency.click()
        except:
            print("Desired currency is chosen already")
            close_modal = self.find_element(By.CSS_SELECTOR, 'button[data-bui-ref="modal-close"]')
            close_modal.click()

    def select_destination(self, destination):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(destination)

        search_input = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        search_input.click()

    def select_date(self, check_in_date, check_out_date):
        check_in_input = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        check_in_input.click()
        check_out_input = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        check_out_input.click()

    def select_adults(self,count=1):
        select_element = self.find_element(By.ID, "xp__guests__toggle")
        select_element.click()