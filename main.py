from users import user_password, user_name
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self, user_name, user_password):
        self.browser = webdriver.Chrome()
        self.user_name = user_name
        self.user_password = user_password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element(by="xpath", value="//*[@id='login_field']").send_keys(self.user_name)
        self.browser.find_element(by="xpath", value="//*[@id='password']").send_keys(self.user_password)
        time.sleep(1)
        self.browser.find_element(by="xpath", value="//*[@name='commit']").click()

    def getFollowers(self):
        self.browser.get("https://github.com/kadrzeybek?tab=followers")
        time.sleep(2)
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")

        for item in items:
            follower = item.find_element(By.CSS_SELECTOR, ".f4.Link--primary").text
            self.followers.append(follower)


github = Github(user_name, user_password)
#github.signIn()
github.getFollowers()
print(github.followers)
