#Script for loading firefox website and extracting title, languages, repo name and further details from github.com/TheDancerCodes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
option = webdriver.FirefoxOptions()
option.add_argument('— incognito')
browser = webdriver.Firefox(executable_path = 'C:/Python27/geckodriver.exe', firefox_options=option)
browser.get('https://github.com/TheDancerCodes')
# Wait 20 seconds for page to load
timeout = 20
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="js-pjax-container"]/div/div[2]/a/img')))
except TimeoutException:
    print('Timed out waiting for page to load')
    browser.quit()
# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[2]/div[3]/h1/span[1]')
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
print('titles:')
print(titles, '\n')
language_element = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div[3]/div[1]/div/ol/li[1]/div/span/a/span')
# same concept as for list-comprehension above.
languages = [x.text for x in language_element]
print('languages:')
print(languages,'\n')
for title, language in zip(titles, languages):
    print('RepoName : Language')
    print(title + ": " + language, '\n')
