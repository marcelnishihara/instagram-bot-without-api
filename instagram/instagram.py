'''
Module instagram
'''


import json

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Instagram:
    '''
    Class Instagram
    '''

    def __init__(
            self,
            user: str,
            password: str,
            time_sleep: int = 10,
            chromedriver: str = './tools/chromedriver.exe') -> None:
        self.user = user
        self.passwd = password
        self.time_sleep = time_sleep
        self.paths = []
        self.list_of_users = []
        self.webdriver = webdriver.Chrome(executable_path=chromedriver)


    def get_paths(self) -> None:
        '''
        Method get_paths()
        '''
        paths_file = open(
            file='./source/paths.json',
            mode='r',
            encoding='utf-8')

        self.paths = json.loads(s=paths_file.read())
        paths_file.close()


    def get_instagram(self) -> None:
        '''
        Method get_instagram()
        '''
        self.webdriver.get(url=f'https://instagram.com/{self.user}')
        sleep(self.time_sleep)


    def extract(self) -> None:
        '''
        Method Sign-in
        '''
        for xpath in self.paths[0]:
            element = self.webdriver.find_element(
                by=By.XPATH,
                value=self.paths[0][xpath])

            keys = None

            if 'username' in xpath:
                keys = self.user
            elif 'password' in xpath:
                keys = self.passwd
            elif 'field_2fa' in xpath:
                keys = input('Insert 2FA Code: ')

            if 'btn_' in xpath:
                element.click()
                sleep(self.time_sleep)
            elif 'field_' in xpath and keys is not None:
                element.send_keys(keys)
                sleep(self.time_sleep)
            elif 'cls_' in xpath:
                element.click()
                sleep(self.time_sleep)

                followers = self.webdriver.find_elements(
                    by=By.CSS_SELECTOR,
                    value='div[role="dialog"] div[role="dialog"] ul li')

                self.list_of_users = [follower.text for follower in followers]


    def scroll_down(self) -> None:
        '''
        Method scroll_down
        '''
        previous_height = self.webdriver.execute_script(
            script='return document.body.scrollHeight')

        self.webdriver.execute_script(
            script='window.scrollTo(0, document.body.scrollHeight)')

        WebDriverWait(driver=self.webdriver, timeout=self.time_sleep).until(
            EC.text_to_be_present_in_element(
            (By.TAG_NAME, 'body'),
            str(previous_height)))
