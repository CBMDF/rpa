from plugins.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Expresso(Browser):

    LOGIN_USERNAME_SELECTOR = '//*[@id="user"]'
    LOGIN_PASSWORD_SELECTOR = '//*[@id="passwd"]'
    LOGIN_SUBMIT_SELECTOR = '/html/body/div[1]/div[2]/div/div[1]/div/div/form/div/div[1]/div[3]/input[2]'
    LOGOUT_SELECTOR = '//*[@id="logout_id"]'
    SEARCH_OPEN_SELECTOR = '/html/body/div[7]/table/tbody/tr/td/div[2]/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/img[1]'
    SEARCH_FROM_SELECTOR = "//input[@id='txt_de']"
    SEARCH_TO_SELECTOR = "//input[@id='txt_para']"
    SEARCH_BODY_SELECTOR = "//input[@id='txt_body']"
    SEARCH_SUBJECT_SELECTOR = "//input[@id='txt_ass']"
    SEARCH_START_DATE_SELECTOR = "//input[@id='since_date']"
    SEARCH_END_DATE_SELECTOR = "//input[@id='before_date']"
    SEARCH_ON_DATE_SELECTOR = "//input[@id='on_date']"
    SEARCH_INBOX_FOLDER_SELECTOR = "//span[@class = 'folder inbox']"
    SEARCH_SELECT_FOLDERS_SELECTOR = '//*[@id="incluir"]'
    SEARCH_BUTTON = "(//button[contains(@class,'ui-button ui-widget')])[3]"

    def __init__(self):
        super().__init__()

    def login(self, url, username, password):
        self.openUrl(url)
        self.fill(self.LOGIN_USERNAME_SELECTOR, username)
        self.fill(self.LOGIN_PASSWORD_SELECTOR, password)
        self.click(self.LOGIN_SUBMIT_SELECTOR)

    def logout(self):
        self.click(self.LOGOUT_SELECTOR)

    def search_message(self, search_query={"from": '', "to": '', "body": '', "subject": '', "start_date": '', "end_date": '', "on_date": ''}):

        # Search button
        self.click(self.SEARCH_OPEN_SELECTOR)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "txt_de")))

        # From
        if search_query.get('from', '') != '':
            self.fill(self.SEARCH_FROM_SELECTOR, search_query['from'])

        # Subject
        if search_query.get('subject', '') != '':
            self.fill(self.SEARCH_SUBJECT_SELECTOR, search_query['subject'])

        # Date start and Date end
        if search_query.get('start_date', '') != '' and search_query.get('end_date', '') != '':
            super().fill(self.SEARCH_START_DATE_SELECTOR,
                         search_query['start_date'])
            super().fill(self.SEARCH_END_DATE_SELECTOR,
                         search_query['end_date'])
        # On date
        if search_query.get('on_date', '') != '':
            self.fill(self.SEARCH_ON_DATE_SELECTOR, search_query['on_date'])
            super().clear(self.SEARCH_START_DATE_SELECTOR)
            super().clear(self.SEARCH_END_DATE_SELECTOR)

        # Select folder
        self.click(self.SEARCH_INBOX_FOLDER_SELECTOR)

        # Move selected
        self.click(self.SEARCH_SELECT_FOLDERS_SELECTOR)

        # Search
        self.click(self.SEARCH_BUTTON)
