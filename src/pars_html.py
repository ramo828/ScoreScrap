from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from lib.smartlib import ParserTools, Log
from tqdm import tqdm
import traceback as tcb
import settings as ayar

pt = ParserTools()
log = Log()
chrome_options = Options()

if(ayar.htmlParserHeadless):
    chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
wait = WebDriverWait(driver, ayar.htmlParserTimeOut)

def miningData(url):
    try:
        driver.get(url)
        gozleme = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="tbTeamHistoryStat_A_all"]')))
        header = gozleme.find_element(By.XPATH,'//*[@id="tbTeamHistoryStat_A_all"]/tbody')
        gozleme1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".zrqst3")))
        g_header = gozleme1.find_elements(By.CSS_SELECTOR,".zrqst3 td")
        gozleme2 = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="tbTeamGoalCountA"]/tbody')))
        g_count = gozleme2.find_element(By.XPATH,'//*[@id="tbTeamGoalCountA"]/tbody/tr[3]')
        g_count = g_count.text.split(" ")
        gozleme3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbTeamGoalStatsA"]')))
        g_history = gozleme3.find_element(By.XPATH, '//*[@id="tbTeamGoalStatsA"]/tbody')
        gozleme4 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tbTeamOddsstatA"]')))
        g_s = gozleme4.find_element(By.XPATH, '//*[@id="tbTeamOddsstatA"]/tbody')
        latest_label = g_s.find_elements(By.CSS_SELECTOR,".zrqst3 td")
        latest_label = pt.web_to_list(latest_label)[1:]
        g_history = g_history.text.splitlines()[1:]
        g_h_data1 = pt.split_two(g_history[0]).split(",")
        g_h_data2 = g_history[1].split(" ")[1:]
        g_h_data3 = g_history[2].split(" ")
        g_h_data4 = g_history[3].split(" ")[1:]
        g_h_data5 = g_history[4].split(" ")
        g_h_data6 = g_history[5].split(" ")[1:]
        g_h_data7 = g_history[6].split(" ")
        g_h_data8 = g_history[7].split(" ")[1:]
        g_h_data9 = g_history[8].split(" ")
        g_s = g_s.text.splitlines()[10:]
        g_s_data1 = latest_label
        g_s_data2 = g_s[1].split(" ")[1:]
        g_s_data3 = g_s[2].split(" ")
        g_s_data4 = g_s[3].split(" ")[1:]
        g_s_data5 = g_s[4].split(" ")
        g_s_data6 = g_s[5].split(" ")[1:]
        g_s_data7 = g_s[6].split(" ")
        g_s_data8 = g_s[7].split(" ")[1:]
        g_s_data9 = g_s[8].split(" ")
        pt.extract3(
                g_s_data1,
                g_s_data2,
                g_s_data3,
                g_s_data4,
                g_s_data5,
                g_s_data6,
                g_s_data7,
                g_s_data8,
                g_s_data9,
                fileName=ayar.dataThreeName
                )
        pt.extract3(
                g_h_data1,
                g_h_data2,
                g_h_data3,
                g_h_data4,
                g_h_data5,
                g_h_data6,
                g_h_data7,
                g_h_data8,
                g_h_data9,
                fileName=ayar.dataFourName
                )

        pt.extract2(g_header, g_count, fileName=ayar.dataTwoName)
        pt.extract1(header, fileName=ayar.dataOneName)
    except Exception as Error:
        print(Error)
        tcb.print_exc()
        log.write(str(Error))
        return
# miningData('https://analyse.7msport.com/4322559/index.shtml')
c = 0

with open(ayar.outputLinkFileName) as lnk:
    for ldata in tqdm(lnk.read().splitlines()):
        if(ldata == ''):
            continue
        miningData(ldata)

