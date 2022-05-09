from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import random

class printablesbot(object):
    def __init__(self):
        
            
      while True:
          self.driver = webdriver.Firefox(executable_path=r"C:\Users\Xavier D'acron\Downloads\geckodriver-v0.29.1-win64\geckodriver.exe")
          self.driver.get('https://www.blockaway.net/')
          sleep(15)
          self.driver.find_element_by_xpath('//*[@id="url"]').send_keys('https://www.printables.com/')
          self.driver.find_element_by_xpath('//*[@id="url"]').send_keys(Keys.ENTER)
          sleep(30)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/header/app-header-sticky/div/nav/div/ul/li[3]/a/i').click()
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/app-search-autocomplete/div[1]/div/form/input').send_keys('mrtprkl')
          sleep(20)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/app-search-autocomplete/div[2]/div/app-search-autocomplete-section[2]/section/div/div/div/a/span').click()
          sleep(20)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-sticky-sidebar/main/div/div/div[2]/ng-component/div/print-card[1]/div/div/h3/a').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/div[2]/div/ul/li[2]/a/div').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/main/app-market-files/div/app-market-downloads/div[1]/div').click()
          sleep(20)
          self.driver.find_element_by_xpath('/html/body/ngb-modal-window/div/div/app-login-modal/button/i').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/div[1]/div/div[2]/div[1]/app-market-detail-user/div/a/span').click()
          sleep(10)
          #2nd
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-sticky-sidebar/main/div/div/div[2]/ng-component/div/print-card[2]/div/div/h3/a').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/div[2]/div/ul/li[2]/a/div').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/main/app-market-files/div/app-market-downloads/div[1]/div').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/div[1]/div/div[2]/div[1]/app-market-detail-user/div/a/span').click()
          sleep(10)
          #3rd
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-sticky-sidebar/main/div/div/div[2]/ng-component/div/print-card[3]/div/div/h3/a').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/div[2]/div/ul/li[2]/a/div').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/main/app-market-files/div/app-market-downloads/div[1]/div').click()
          sleep(10)
          self.driver.find_element_by_xpath('/html/body/app-root/app-baselayout/div/div/ng-component/app-market-detail/div[1]/div/div[2]/div[1]/app-market-detail-user/div/a/span').click()
          sleep(10)
          self.driver.close()
          sleep(20)
          
          


      

       
printablesbot()

