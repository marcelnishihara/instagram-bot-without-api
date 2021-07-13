import tools.instagram as ig

from selenium import webdriver
from tools.credentials import credentials as creds
from tools.helpers import log_lists_to_file


if __name__ == '__main__':
    chrome_session = webdriver.Chrome('tools/chromedriver')
    
    ig.login(driver=chrome_session, time_sleep=3)
    
    following = ig.get_list(
        driver=chrome_session, 
        which_list='following',
        time_sleep=3)
    
    followers = ig.get_list(
        driver=chrome_session, 
        which_list='followers',
        time_sleep=3)

    chrome_session.quit()
    
    username = creds['username']
    lists = { 'following' : following, 'followers' : followers }
    
    log_msg = log_lists_to_file(
        username=username, 
        dict_to_log=lists)
    
    print(log_msg)