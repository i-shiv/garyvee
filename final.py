from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import sys
import time
import string

class GaryVee:
    username = input("Enter username")
    password = input("Enter Password")

    hashtags = [
        'wanderlust', 'travels', 'travel', 'explore', 'exploring', 
        'vacation', 'adventure', 'holiday', 'holidays', 'instatravel',
    ]
    
    

    

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.login()
        self.execute()


    def login(self):
        self.browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)

        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username)
        time.sleep(1)

        password_field = self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password)
        time.sleep(1)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        time.sleep(5)
    

    def execute(self):
        for hashtag in self.hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/' + hashtag +'/')
            time.sleep(2)
            a=self.browser.find_elements_by_class_name("_9AhH0")
            comments = [
                'Your posts are amazing', 'Amazing photo. Keep going!', 'Your photos are magnificent',
                'Your work fascinates me!', 'I like how you put your posts together',
                'What a really nice photo, great job!', 'Well done!', 'Your posts are amazing']

            
            for i in range(0,9):
                a[i].click()
                time.sleep(5)
                b=self.browser.find_element_by_class_name("wpO6b")
                b.click()
                time.sleep(5)
                c=self.browser.find_element_by_class_name("Ypffh")
                c.click()
                time.sleep(2)
                v=random.choice(comments)
                c=self.browser.find_element_by_class_name("Ypffh.focus-visible").send_keys(v)
                time.sleep(1)
                self.browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button").click()
                time.sleep(5)
                self.browser.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
                
                

garyVee = GaryVee()
                