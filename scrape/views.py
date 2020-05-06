from django.shortcuts import render
from django.http import HttpResponse
import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json
import itertools
# the relevant url


# Create your views here.
def index(request):
	fi = fetch()
	return render(request, "index.html", {"score": fi})


"""def fetch_imagery():
	url = 'https://web.bet9ja.com/Sport/OddsToday.aspx?IDSport=590'
	driver = webdriver.Chrome(r"c:/Users/my-project/mysite/chromedriver")
	driver.get(url)
	driver.implicitly_wait(10) # seconds
	buttons = WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Event.ng-binding")))
	for btn in range(len(buttons)):
		buttons = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Event.ng-binding")))
		buttons[btn].click()
		headings= [item.text for item in driver.find_elements_by_css_selector("div.SECQ.ng-binding")]
		keys = [item.text for item in driver.find_elements_by_css_selector("div.SEOdd.g1")]
		values = [item.text for item in driver.find_elements_by_css_selector("div.SEOddLnk.ng-binding")]
		driver.execute_script("window.history.go(-1)")
		score_list_list=headings,keys,values
		print(score_list_list)
	return score_list_list"""




"""def fetch_imagery():
	url = 'https://web.bet9ja.com/Sport/SubEventDetail?SubEventID=78706980'
	driver = webdriver.Chrome(r"chromedriver")
	driver.get(url)
	driver.implicitly_wait(10) # seconds
	elements = [item.text for item in driver.find_elements_by_css_selector("div.SEOddLnk.ng-binding")]
	names = [item.text for item in driver.find_elements_by_css_selector("div.SECQ.ng-binding")]
	headings=names[0:3]+names[27:31]+names[85:87]+names[61:63]+names[88:90]
	values = [item.text for item in driver.find_elements_by_css_selector("div.SEOddsTQ.ng-binding")]
	keys=values[0:8]+values[148:156]+values[244:248]+values[348:352]
	vals=elements[0:8]+elements[148:156]+values[244:248]+values[348:352]
	score_list_list=[
	['bet9ja.com',headings[0] , keys[0] , vals[0] , keys[1] , vals[1] , keys[2], vals[2]],
	['bet9ja.com',headings[1] , keys[3] , vals[3] , keys[4] , vals[4] , keys[5], vals[5]],
	['bet9ja.com',headings[2] , keys[6] , vals[6] , keys[7] , vals[7]], 
	['bet9ja.com',headings[3] , keys[8] , vals[8] , keys[9] , vals[9]], 
	['bet9ja.com',headings[4] , keys[10] , vals[10] , keys[11] , vals[11]],
	['bet9ja.com',headings[5] , keys[12] , vals[12] , keys[12] , vals[12]],
	['bet9ja.com',headings[6] , keys[13] , vals[13] , keys[14] , vals[14]],
	]
	for score in score_list_list:
		return score_list_list


def fetch_imager():
	url = 'https://www.betking.com/sports/s/event/p/soccer/turkmenistan/tkm-yokary-liga/0/0'
	driver = webdriver.Chrome(r"chromedriver")
	driver.get(url)
	driver.implicitly_wait(10) # seconds
	elements = [item.text for item in driver.find_elements_by_css_selector("th.eventOdds")]
	names = [item.text for item in driver.find_elements_by_css_selector("th.headers")]
	values = [item.text for item in driver.find_elements_by_css_selector("div.oddBorder")]
	button = driver.find_element_by_xpath('//*[@id="match_2509424"]/td[11]/span')
	driver.execute_script("arguments[0].click();", button)
	headers = [item.text for item in driver.find_elements_by_css_selector("div.headerText")]
	headings=elements[1:4]+headers[3:7]
	names1 = [item.text for item in driver.find_elements_by_css_selector("div.inner-content.eventPopup > span")]
	keys=names[0:8]+names1[38:46]
	values1 = [item.text for item in driver.find_elements_by_css_selector("div.oddBorder")]
	vals=values[0:8]+values1[38:46]
	row_list_list=[['betking.com',headings[0] , keys[0] , vals[0] , keys[1] , vals[1] , keys[2], vals[2]],
	['betking.com',headings[1] , keys[3] , vals[3] , keys[4] , vals[4] , keys[5], vals[5]],
	['betking.com',headings[2] , keys[6] , vals[6] , keys[7] , vals[7]],
	['betking.com',headings[3] , keys[8] , vals[8] , keys[9] , vals[9]], 
	['betking.com',headings[4] , keys[10] , vals[10] , keys[11] , vals[11]],
	['betking.com',headings[5] , keys[12] , vals[12] , keys[12] , vals[12]],
	['betking.com',headings[6] , keys[13] , vals[13] , keys[14] , vals[14]]]
	for row in row_list_list:
		return row_list_list"""

def fetch():
	url = 'https://web.bet9ja.com/Sport/OddsToday.aspx?IDSport=590'
	driver = webdriver.Firefox()
	driver.get(url)
	driver.implicitly_wait(10) # seconds
	buttons = WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Event.ng-binding")))
	for btn in range(len(buttons)):
		if(btn==1):
			buttons = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.Event.ng-binding")))
			buttons[btn].click()
			classes = [item.text for item in driver.find_elements_by_css_selector("div.SEItem.ng-scope")]
			driver.execute_script("window.history.go(-1)")
			clases = [elem.strip().split('\n') for elem in classes]
			for li in clases:
				li.remove('open')
	score_list_list = clases
	print(score_list_list)
	filled_arr = list(zip(*itertools.zip_longest(*score_list_list, fillvalue='#')))
	for score in filled_arr:
		return filled_arr
