from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from tools.credentials import credentials as creds


ig_xpath = {
    'log_in_button' : '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button',
    'username' : '//*[@id="loginForm"]/div/div[1]/div/label/input',
    'password' : '//*[@id="loginForm"]/div/div[2]/div/label/input',
    'six_digit' : '//*[@id="react-root"]/section/main/div/div/div[1]/div/form/div[1]/div/label/input',
    'deny_save_info' : '//*[@id="react-root"]/section/main/div/div/div/div/button',
    'followers' : '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a',
    'following' : '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a',
    'css_selector' : '.FPmhX.notranslate._0imsa ',
    'close_list' : '/html/body/div[5]/div/div/div[1]/div/div[2]/button'
}


def login(driver: webdriver, time_sleep: int = 2) -> None:
    """It writes username and password from tools/credentials.py 
    file into browser session.

    Slower internet connections requires values greater than 
    default number for the parameter time_sleep. Default value
    is 2.

    Args:
        driver (webdriver): A Selenium WebDriver.
        
        time_sleep (int): Time in seconds that the script is 
            going to wait until interact to the next element 
            of the page.
    """
    
    ig_url = 'https://instagram.com/'
    ig_profile = creds['username']

    driver.get(f'{ig_url}{ig_profile}')
    sleep(time_sleep)

    driver.find_element_by_xpath(ig_xpath['log_in_button']).click()
    sleep(time_sleep)

    driver.find_element_by_xpath(ig_xpath['username']).send_keys(creds['username'])
    sleep(time_sleep)

    password_input = driver.find_element_by_xpath(ig_xpath['password'])
    password_input.send_keys(creds['password'])
    password_input.send_keys(Keys.ENTER)
    
    six_digit = input('Insert the Six Digit Code: ') 
    six_digit_input = driver.find_element_by_xpath(ig_xpath['six_digit'])
    six_digit_input.send_keys(int(six_digit))
    six_digit_input.send_keys(Keys.ENTER)
    sleep(time_sleep)

    driver.find_element_by_xpath(ig_xpath['deny_save_info']).click()
    sleep(time_sleep)


def get_list(driver: webdriver, which_list: str = 'followers', time_sleep: int = 2) -> list:
    """Interacts with the webdriver and get the Instagram username 
    (set in the tools/credentials.py file) followers or following 
    list.

    Args:
        driver (webdriver): A Selenium WebDriver.
        which_list (str): Select the followers or following list.
        time_sleep (int): Time in seconds that the script is 
            going to wait until interact to the next element 
            of the page.

    Returns:
        list: Followers or following list of the username.
    """
    if which_list == 'followers' :
        which_list = ig_xpath['followers']
    elif which_list == 'following' :
        which_list = ig_xpath['following']

    driver.find_element_by_xpath(which_list).click()
    sleep(time_sleep)

    js_comand='''
    let followers = document.querySelector(".isgrP")
    followers.scrollTo(0, followers.scrollHeight)
    let lenOfPage = followers.scrollHeight
    return lenOfPage
    '''

    length_of_page = driver.execute_script(js_comand)
    match = False

    while(match==False):
        last_count = length_of_page
        sleep(time_sleep)
        length_of_page = driver.execute_script(js_comand)
        if last_count == length_of_page : match = True
    
    sleep(time_sleep)

    followers = driver.find_elements_by_css_selector(ig_xpath['css_selector'])

    followers_list = []
    
    for follower in followers:
        followers_list.append(follower.text)

    driver.find_element_by_xpath(ig_xpath['close_list']).click()

    return followers_list
