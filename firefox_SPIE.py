
# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from fake_useragent import UserAgent
from collections import defaultdict
import pandas as pd
import random
import time
import os
import re
import json

# =============================================================================
# 
# =============================================================================

def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, {});'.format(random.randint(-350,-250))
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)
    
def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)

def click_locxy(dr, x, y, left_click=True):
    if left_click:
        ActionChains(dr).move_by_offset(x, y).click().perform()
    else:
        ActionChains(dr).move_by_offset(x, y).context_click().perform()
    ActionChains(dr).move_by_offset(-x, -y).perform()  # 將滑鼠位置恢復到移動前

# =============================================================================
# 
# =============================================================================

yearFrom = 2017
yearTo   = 2021
start_url = r"https://www.spiedigitallibrary.org/conference-proceedings-of-spie/browse/SPIE-Advanced-Lithography"
web_url   = r"https://www.spiedigitallibrary.org"

download_dir = os.sep.join([os.getcwd(),"SPIE"])
mime_types = "application/pdf,application/vnd.adobe.xfdf,application/vnd.fdf,application/vnd.adobe.xdp+xml"

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", download_dir)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", mime_types)
fp.set_preference("plugin.disable_full_page_plugin_for_types", mime_types)
fp.set_preference("pdfjs.disabled", True)

browser = webdriver.Firefox(firefox_profile=fp)
browser.maximize_window()
browser.get(start_url)

# with open(f'page_source.txt', 'w') as f:
#     json.dump(browser.page_source, f)
# print(browser.page_source)

recordurl = defaultdict(lambda : dict())
for year in range(yearFrom, yearTo+1):
    yearLink_key = "//div[@id='InnerYearDivspie-advanced-lithography{0}']".format(year)
    yearLinks = browser.find_elements_by_xpath(yearLink_key)
    if len(yearLinks)==0:
        print(f"There is no {year} infomation!")
        continue
    
    scroll_shim(browser, yearLinks[0])
    ActionChains(browser).move_to_element(yearLinks[0]).perform()
    if yearLinks[0].is_displayed():
        yearLinks[0].click()
        items = browser.find_elements_by_xpath("//div[@id='InnerYearItemspie-advanced-lithography{0}']//a[contains(@href,'')]".format(year))
        for item in items:
            if not item.text.isnumeric():
                recordurl[year][item.text] = item.get_attribute("href")

articleurl = defaultdict(lambda : defaultdict(lambda : defaultdict(list)))
for year, item1 in recordurl.items():
    for className, url in item1.items():
        browser.get(url)
        time.sleep(random.randint(1,3))
        items = browser.find_elements_by_xpath("//div[@style='padding:0;margin:0;width:100%;']")
        for i, item in enumerate(items):
            if i <= 1: continue
            subTitle = item.get_attribute('id')[3:-len("LINEITEMSTop")]
            
            tmpurl = []
            for a in item.find_elements_by_xpath(".//div[@class='TOCLineItemRowCol1']//a[@class='TocLineItemAnchorText1']"):
                tmpurl.append(a.get_attribute("href"))
            articleurl[year][className][subTitle] = tmpurl


# with open(f'downloadList.json', 'w') as f:
#     json.dump(articleurl, f)

with open('downloadList.json') as f:
    articleurl = json.load(f)

outputData = defaultdict(list)
with open('data_260.json') as f:
    outputData = json.load(f)

CurrentCount = 260
count = 0
for year, item1 in articleurl.items():
    print(year, " ", count)
    for className, item2 in item1.items():
        for subClass, urlList in item2.items():
            for url in urlList:
                count += 1
                if count <= CurrentCount: continue
                
                browser.get(url)
                time.sleep(random.randint(5,60))
                
                button = browser.find_element_by_xpath("//a[@class='ProceedingsArticleOpenAccessAnchorText']")
                if button:
                    scroll_shim(browser, button)
                    ActionChains(browser).move_to_element(button).perform()
                    if button.is_displayed():
                        button.click()
                time.sleep(random.randint(1,3))
                
                title = abstract = conclusion = ""
                authors = companys = []
                
                try:
                    title   = browser.find_element_by_xpath("//text[@class='ProceedingsArticleOpenAccessHeaderText']").text
                    authors = [a.text for a in browser.find_element_by_xpath("//text[@class='ProceedingsArticleOpenAccessText']").find_elements_by_xpath(".//*")]
                    companys= re.findall(r"\d([^1-9]+)",browser.find_element_by_xpath("//div[@id='affiliations']").text.split("\n")[-1])
                    abstract= browser.find_element_by_xpath("//text[@class='ArticleContentText']").text
                    
                    conclusion = []
                    for item in browser.find_elements_by_xpath("//div[@id='article-body']/div[3]//p"):
                        scroll_shim(browser, item)
                        conclusion.append(item.text)
                        time.sleep(random.randint(3,10))
                    conclusion = "\n".join(conclusion)
                    # conclusion = "\n".join([item.text for item in browser.find_elements_by_xpath("//div[@id='article-body']/div[3]//p")])
                                        
                except Exception as e:
                    print([year, className, url])
                    print(e)
                    continue
                
                outputData["Year"].append(year)
                outputData["mainClass"].append(className)
                outputData["subClass"].append(subClass)
                outputData["url"].append(url)
                outputData["title"].append(title)
                outputData["authors"].append(authors)
                outputData["companys"].append(companys)
                outputData["abstract"].append(abstract)
                outputData["conclusion"].append(conclusion)
                if count%20 == 0:
                    print(f"Finish {count}")
                    with open(f'data_{count}.json', 'w') as f:
                        json.dump(outputData, f)
                    

browser.close()
