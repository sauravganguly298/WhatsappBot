import sys
import sys as system
import time as t
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#This function is used to search and invoke the first user
def search_user(username):
    try:
        chat_new = browser.find_element(By.XPATH,value="//body/div[@id='app']/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[1]")
        chat_new.click()
        search_box = browser.find_element(By.XPATH, value="//div[@title='Search input textbox']")
        search_box.send_keys(username)
    except Exception as E:
        print(f"The {username} is not present")
        print(E.__cause__)

#This is the function to find the user chat
def user_chat(username,message,no_of_times=1):
    try:
        user = browser.find_element(By.XPATH,value="//span[@title='{}']".format(username))
        user.click()
        textbox = browser.find_element(By.XPATH,value="//body/div[@id='app']/div[1]/div[1]/div[4]/div[1]/footer[1]/div[1]/div[1]/span[2]/div[1]/div[2]/div[1]")
        for i in range(no_of_times):
            textbox.send_keys(message)
            send = browser.find_element(By.XPATH, value="//button[@data-testid='compose-btn-send']")
            send.click()
    except Exception as E:
        print("The message cann't be sent sorry")
        print(E.__cause__)

#This is the full function that will do the chat
def spam(username,message,no_of_times=1):
    search_user(username)
    user_chat(username,message,no_of_times)

#This is the function which will run if the file is ran as the main function
if __name__ == '__main__':
    user_name = input("Enter the name to be messaged : ")
    message = input("Enter the message to be sent: ")
    no_of_times = int(input("Enter the no of times the message to be sent : "))
    choice = int(input('''
    Enter:
    1:To Spam
    2:To message once
    3:To Exit\n'''))
    if(choice==3):
        exit(1)
    my_options = webdriver.ChromeOptions()
    my_options.add_argument("user-data-dir=C:\\Users\\aman_\\AppData\\Local\\Google\\Chrome\\User Data\\Profile8")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=my_options)
    browser.get("https://web.whatsapp.com")
    browser.implicitly_wait(30)
    if(choice == 1):
        spam(user_name,message,no_of_times)
    elif choice == 2:
        spam(user_name,message)







