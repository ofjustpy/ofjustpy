import os

import logging
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/usr/bin/chromedriver"

# ============================ setup logs ============================
try:
    os.remove("browser.log")
except:
    pass

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(filename="browser.log",
                    level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger(__name__)
# ================================ end ===============================


#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser:
    def __init__(self, **kwargs):
        self.options = webdriver.ChromeOptions()
        # self.options.headless = True
        self.options.add_argument("--headless")
        self.browser = webdriver.Chrome(
            options=self.options, service=Service(path))

    def __enter__(self):
        return self

    def get_page(self, url, wait_secs, label=None):
        self.browser.get(url)
        WebDriverWait(self.browser, wait_secs).until(lambda driver: driver.execute_script(
            'return document.readyState') == 'complete')  # or when says go
        yield "wait done"
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        html = soup.prettify("utf-8")
        yield html

        if label is not None:
            with open(label + ".html", "wb") as file:
                file.write(html)

    def element_exists(self, element_id):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.ID, element_id))
            )   #wait for page to load, so element with ID 'username' is visible
        except :

            return False
        
        return True

    def set_element_text(self, element_id, text):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.ID, element_id))
            )   #wait for page to load, so element with ID 'username' is visible
        except :
            logging.info(f"Could not find element {element_id}")
            return False
        
        if element:
            element.send_keys(text)
            return True
        
        return False

    def get_element_text(self, element_id):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.ID, element_id))
            )   #wait for page to load, so element with ID 'username' is visible
        except :
            logging.info(f"Could not find element {element_id}")
            
            return None
        
        try:
            value = element.text
        except:
            value = None
        logging.info (f"Value = {element.text}")
        return value


    
    def get_element_attr_value(self, element_id, attr):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.ID, element_id))
            )   #wait for page to load, so element with ID 'username' is visible
        except :
            logging.info(f"Could not find element {element_id}")
            return False
        
        try:
            value = element.get_attribute(attr)
        except:
            logging.info(f"Could not find attr {attr} for element {element_id}")
            value = None
        return value
        
    def submit_element(self, element_id):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.ID, element_id))
            )   #wait for page to load, so element with ID 'username' is visible
        except :
            logging.info(f"Could not find element {element_id}")
            return False

        try:
            element.click()
        except Exception as e:
            logging.info(f"Could not click  element {element_id}: {e}")
        return True

    def is_selected(self, element_id):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.ID, element_id))
            )   #wait for page to load, so element with ID 'username' is visible
        except :
            logging.info(f"Could not find element {element_id}")
            return None

        try:
            cbox_value = element.is_selected()
        except Exception as e:
            logging.info(f"Could not is_selected {element_id}: {e}")
            return None
        
        return cbox_value
    

    def check_if_tag_text_pair_exists(self, tag_name, text):
        logging.debug(f"Called with {tag_name} {text}")
        try:
            wait = WebDriverWait(self.browser, 5)
            elements = wait.until(
                EC.presence_of_all_elements_located((By.TAG_NAME, tag_name))
            )   #wait for page to load, so element with ID 'username' is visible
        except Exception as e:
            logging.debug(f"Could not find tag_name {tag_name}: {e}")
            print(e)
            return None
        
        for element in elements:
            print("checking element ", element.text)
            if element.text == text:
                return True
            
        return False



    def __exit__(self, type, value, traceback):
        self.browser.quit()
