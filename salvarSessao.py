from selenium import webdriver
import pickle

browser = webdriver.Chrome('./chromedriver')

browser.get('https://web.whatsapp.com/')

salvarBrowser = input()

if salvarBrowser == "sim":
    pickle.dump(browser, open("cookies.pkl","wb"))

