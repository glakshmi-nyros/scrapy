# Here using selenium for scraping
# importing necessary modules
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# the relevant url
url = 'https://web.bet9ja.com/Sport/OddsToday.aspx?IDSport=590'

# the driver path
driver = webdriver.Chrome(r"c:/Users/SATYA/mysite/chromedriver")
driver.get(url)
driver.implicitly_wait(10) # seconds
buttons = WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Event.ng-binding")))
for btn in range(len(buttons)):
    #elements re-assigned again to avoid stale.
    buttons = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Event.ng-binding")))
    buttons[btn].click()
    headings= [item.text for item in driver.find_elements_by_css_selector("div.SECQ.ng-binding")]
    keys = [item.text for item in driver.find_elements_by_css_selector("div.SEOdd.g1")]
    values = [item.text for item in driver.find_elements_by_css_selector("div.SEOddLnk.ng-binding")]
    driver.execute_script("window.history.go(-1)")
    print(headings,keys,values)