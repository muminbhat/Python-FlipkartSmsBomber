from time import sleep
from selenium import webdriver
import time

#Create Instance of FireFox Browser
driver = webdriver.Firefox() 

#Set the frequency of sms which is approx maximum to 10 per 24 days
frequency = 1

#Target Mobile Number
mobile_number = 7051675193 #Set the input for mobile_number

for i in range(frequency):

    #Open Flipkart login page
    driver.get("https://www.flipkart.com/account/login?ret=/")

    driver.maximize_window()

    #Element where we have to enter the phone numebr
    element = driver.find_element_by_xpath("//input[@class='_2IX_2- VJZDxU']")

    #Phone number to send sms to 
    element.send_keys("7051675193")

    #find the element to send a forgot password
    otp = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3NgS1a']")

    otp.click()
    time.sleep(2)

#Close the browser
driver.quit()
