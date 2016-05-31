#! /usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from random import randint

file = open("words")
text = file.read()
text = text.split("\n")
text = sorted(list(set(text)))
file.close()

browser = webdriver.Firefox()

def instagc_login_page():
    browser.get("http://www.instagc.com/users/login")


def login():
    userField = browser.find_element_by_css_selector("#username")
    userField.click()
    userField.send_keys("********")
    passField = browser.find_element_by_css_selector("#password")
    passField.click()
    passField.send_keys("********")
    loginButton = browser.find_element_by_css_selector(".action")
    loginButton.click()

def goto_search_page():
    browser.get("http://www.instagc.com/search/")

def search_words():
    x = text[randint(0,len(text))] + " " + text[randint(0,len(text))]
    return x

def search():
    searchField = browser.find_element_by_css_selector("#q")
    searchField.click()
    searchField.send_keys(search_words())
    searchButtonSelector = ".validate > button:nth-child(2)"
    searchButton = browser.find_element_by_css_selector(searchButtonSelector)
    searchButton.click()

def link_clicker():
    browser.switch_to_frame("ypaAdWrapper-IN_Algo-iframe")
    links = browser.find_elements_by_css_selector("a.ypaAdAnchor")
    x = links[randint(0,len(links)-1)]
    x.click()

def close_result_window():
    time.sleep(randint(1,16))
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    x = browser.find_element_by_css_selector("body")
    x.send_keys(Keys.CONTROL + 'w')

def switch_to_main():
    browser.switch_to_window(browser.window_handles[0])

instagc_login_page()
login()
time.sleep(randint(1,11))
def main():
    while True:
        goto_search_page()
        search()
        link_clicker()
        close_result_window()
        time.sleep(randint(0,11))
        switch_to_main()
        time.sleep(randint(0,11))

if __name__ == "__main__":
    main()
