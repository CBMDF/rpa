from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.common.keys import Keys
import platform
import os
import time
from plugins import Plugin


class Browser(Plugin):

    METHOD_XPATH = "XPATH"
    METHOD_ID = "ID"
    METHOD_LINK_TEXT = "LINK_TEXT"
    METHOD_CSS_SELECTOR = "CSS_SELECTOR"

    profile_path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'firefox-profile')
    downloadPath = os.path.join(profile_path, "Downloads")
    mimeTypes = "application/zip,application/octet-stream,application/pdf"
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
    profile = webdriver.FirefoxProfile(profile_path)

    profile.set_preference("security.default_personal_cert",
                           "Select Automatically")
    profile.set_preference('webdriver.firefox.logfile', profile_path)

    profile.set_preference('browser.download.folderList', 2)  # custom location
    profile.set_preference('browser.download.manager.showWhenStarting', False)
    profile.set_preference("browser.download.manager.focusWhenStarting", False)
    profile.set_preference("browser.download.manager.useWindow", False)
    profile.set_preference(
        "browser.download.manager.showAlertOnComplete", False)
    profile.set_preference("browser.download.dir", downloadPath)
    profile.set_preference("browser.helperApps.alwaysAsk.force", False)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", mimeTypes)
    profile.set_preference("browser.download.panel.shown", True)

    driver = webdriver.Firefox(firefox_profile=profile)

    driver.set_window_size(1094, 695)
    # wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)  # seconds

    def __init__(self, profilePath=''):
        super().__init__()

    def __del__(self):
        self.driver.get_screenshot_as_file('tela.png')
        time.sleep(5)
        self.driver.quit()

    def openUrl(self, url):
        self.driver.get(url)
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(10)

    def click(self, element):
        self.find_element(element).click()

    def fill(self, element, value):
        elem = self.find_element(element)
        elem.clear()
        elem.send_keys(value)

    def find_element(self, element):

        try:
            found_element = self.driver.find_element_by_id(element)
        except NoSuchElementException:
            try:
                found_element = self.driver.find_element_by_xpath(element)
            except NoSuchElementException:
                try:
                    found_element = self.driver.find_element_by_partial_link_text(
                        element)
                except NoSuchElementException:
                    try:
                        found_element = self.driver.find_element_by_css_selector(
                            element)
                    except NoSuchElementException:
                        raise Exception(
                            'Elemento "{}" não encontrado na DOM'.format(element))

        return found_element
