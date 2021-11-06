from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()

# to run in the background or without opening chrome GUI
# chrome_options.add_argument("--headless")

# open chrome, name the object as driver
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()

# jump to BoM home page
bom_main_page = "https://www.mongolbank.mn/default.aspx"
driver.get(bom_main_page)


# //*[@id='ContentPlaceHolder1_lblRate'] - xpath
# /html/body/form/main/div[2]/div/div/div/div[2]/h1/a/span - Full xpath

policy_rate = driver.find_element(By.XPATH, "//*[@id='ContentPlaceHolder1_lblRate']").text
usd_rate    = driver.find_element(By.ID,'ContentPlaceHolder1_lblUSD').text
spans       = driver.find_elements(By.XPATH,"//*/h1/a/span") # multiple elements 
        # Note that for all find_, if you use elements, the result will be a list, 
        # if element, just first as not list


# loop through exchange rates
daily_fx_page = "https://www.mongolbank.mn/dblistofficialdailyrate.aspx"
driver.get(daily_fx_page)

all_rates_path = "/html/body/form/main/div/div/div/div/div[2]/div/div[5]/ul/li" # list of rates on that date
all_rates = driver.find_elements(By.XPATH, all_rates_path)

for i in range(len(all_rates)-1):
    rate = all_rates[i].find_element_by_xpath("table/tbody/tr/td[3]/span").text # A fx rate
    rate_en = all_rates[i].find_element_by_xpath("table/tbody/tr/td[3]/span").get_attribute("id")[-3:] # FX code, 3 letters
    rate_mn = all_rates[i].find_element_by_xpath("table/tbody/tr/td[2]").text # MN long description of FX code
    print(rate,rate_mn,rate_en, i)
        
     
        
# enter value to input box and search
driver.find_element(By.XPATH, "//*[@id='gsc-i-id1']").send_keys("бодлогын хүү")
driver.find_element(By.XPATH,"//*[@id='___gcse_0']/div/form/table/tbody/tr/td[2]/button").click()


driver.get(daily_fx_page)

# select exchange rate for chosen "year, month, day"
# year
driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_cboYEAR_Input').click()
driver.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_cboYEAR_DropDown']/div/ul/li[2]").click()

# month
driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_cboMONTH_Input').click()
driver.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_cboMONTH_DropDown']/div/ul/li[10]").click()

# day
driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_cboDAY_Input').click()
my_day    = 15
day_xpath = "//*[@id='ctl00_ContentPlaceHolder1_cboDAY_DropDown']/div/ul/li[" + str(my_day) + "]"
driver.find_element(By.XPATH, day_xpath).click()

# load
driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_btnSearch']").click()



# Хайх товчлуурын attributes-ыг харах
driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$btnSearch").get_attribute("value")
driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$btnSearch").get_attribute("type")



# Элемент доторх утгаар хайх
found = driver.find_element(By.XPATH,"//*[contains(text(), 'зарласан')]").text


### Additional

# open new tab - 2 tabs just for example later
driver.execute_script('''window.open();''')
driver.execute_script('''window.open();''')


# switch between tabs
driver.switch_to.window(driver.window_handles[0])
driver.switch_to.window(driver.window_handles[3])
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[2])
driver.switch_to.window(driver.window_handles[-1])

# navigating history
driver.back()      # previous page in browser history
driver.forward()   # next page in browser history


# clear
driver.get(daily_fx_page)
inBox = driver.find_element(By.XPATH, "//*[@id='gsc-i-id1']")
inBox.send_keys("бодлогын хүү")
inBox.clear()


# find by tag name 
h1 = driver.find_element(By.TAG_NAME,"h1")
print(h1.text)
h1 = driver.find_elements(By.TAG_NAME,"h1")
print(h1[0].text)

# find by css selector - Inspect, Copy, Copy Selector
header_date = driver.find_element(By.CSS_SELECTOR,"#ContentPlaceHolder1_lblDate")
print(header_date.text)


driver.get(daily_fx_page)
# find by link_text
rate_link = driver.find_element(By.LINK_TEXT,"Ханшийн статистик")
rate_link.click()

driver.get(daily_fx_page)
# find by partial_link_text
rate_link = driver.find_element(By.PARTIAL_LINK_TEXT,"Ханшийн стат")
rate_link.click()

