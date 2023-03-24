from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from src.lib.smartlib import UrlSniffer
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
import src.settings as ayar


sm = UrlSniffer()

def button(driver, id, page = 1):
    waitButton = WebDriverWait(driver, ayar.urlParserTimeOut)
    if(id < 20):
        page = 1
    else:
        page = 2
        id = id-19
    wbtn = waitButton.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="e_run_tb"]/tbody/tr[{page}]')))
    btn = wbtn.find_element(By.XPATH, f'//*[@id="e_run_tb"]/tbody/tr[{page}]/td[{id}]')
    return btn

chromeOptions = Options()
if(ayar.urlParserHeadless):
    chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chromeOptions)
wait = WebDriverWait(driver, ayar.urlParserTimeOut)
driver.get(ayar.defaultParseUrl)
sleep(3)
counter = 1
page = ""
while True:
    if(counter==39):
        break
    try:
        btn = button(driver, counter)
        sleep(3)
        btn.click()
        pageNumber = btn.text+"#"
        page += pageNumber
        pages = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="Match_Table"]')))
        mch = pages.find_elements(By.TAG_NAME,"a")
        tName = mch[1].text 
        t1Name = mch[3].text 
        # Team name
        # print(f"{pageNumber} - {tName} VS {t1Name}")
        print(page)
        sm.matches(mch)
        sleep(2)
        counter+=1
    except Exception as e:
        print(e)
    
links = sm.filter_unwanted_string(sm.links,"ShowDetails")
links = sm.filter_unwanted_string(links,"'timezone.html'")
links = sm.replace_strings(links,"ShowAnalyse_en(","")
links = sm.unique_values(links)

with open(ayar.outputLinkFileName,"w") as linksFile:
    for link in tqdm(links):
        linksFile.write(link+"\n")
