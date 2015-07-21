from threading import Thread
from bs4 import BeautifulSoup
from urllib2 import urlopen
from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC

BASE_URL = "https://play.google.com"

def get_links(section_url):
	browser = webdriver.Chrome("/Users/jensenkuo/Downloads/chromedriver")
	browser.get(section_url)
	
	actions = AC(browser)
	slow = 0 
	fast = len(browser.page_source)

	while True:											
		try: 
			pass

		except:
			slow = fast
			browser.execute_script("window.scrollBy(0, -10);")
			browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			browser.implicitly_wait(4)
			fast = len(browser.page_source)
		else:
			break
		finally:
			if slow == fast:
				try: 
					showbutton = browser.find_element_by_id("footer-content").find_element_by_tag_name("button")
				except:
					pass
				else:
					actions.click(showbutton).perform()

	html_source = browser.page_source
	soup = BeautifulSoup(html_source, "lxml")
	cardlist = soup.find("div", {"class": "card-list two-cards"})
	links = [BASE_URL + h2.a["href"] for h2 in cardlist.findAll("h2")]
	browser.quit()
	print links
	return links
	

