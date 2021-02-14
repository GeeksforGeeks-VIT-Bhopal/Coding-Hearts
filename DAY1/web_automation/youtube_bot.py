# WINDOWS: pip install selenium
# MAC/LINUX: pip3 install selenium
from selenium import webdriver

# WINDOWS: pip install webdriver_manager
# MAC/LINUX: pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager

# we are using `time` to wait program for 'x' seconds
import time

# doraemon(name can be changed) is the bot that opens Chrome tab 
doraemon = webdriver.Chrome(ChromeDriverManager().install())

# `get` function is used to open any URL (don't forget to use `https://` at start)
doraemon.get('https://youtube.com')

# `find_element_by_xpath` function is used to find element in a web browser
searchBar = doraemon.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')

# `click` function is used to click an element
searchBar.click()

# `send_keys` function is used to write something in an element
searchBar.send_keys('Geeksforgeeks vit bhopal')

searchButton = doraemon.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
searchButton.click()

# `sleep` function will stop the compiler for 'x' seconds
time.sleep(4) 

gfg = doraemon.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-channel-renderer[1]/div')
gfg.click()

time.sleep(2)

vid = doraemon.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-shelf-renderer/div[1]/div[2]/ytd-expanded-shelf-contents-renderer/div/ytd-video-renderer/div[1]')
vid.click()
