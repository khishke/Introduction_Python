
# Request of Munkhtushig

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

chrome_options = Options()

# to run in the background or without opening chrome GUI
chrome_options.add_argument("--headless")

# open chrome, name the object as driver
driver = webdriver.Chrome(chrome_options=chrome_options)

# daily_fx_page = "https://www.mongolbank.mn/dblistofficialdailyrate.aspx"
# driver.get(daily_fx_page)

rates_list = []

for year in range(2019,2019+1):
    for month in range(2,3+1):
        for date in range(1,7+1):
            my_date = "-".join([str(int) for int in [year, month, date]])
            link_date = "https://www.mongolbank.mn/dblistofficialdailyrate.aspx?vYear=" + str(year) + \
            "&vMonth=" + str(month) + "&vDay=" + str(date)
            driver.get(link_date)

            rate_path = "/html/body/form/main/div/div/div/div/div[2]/div/div[7]/ul/li" # list of rates on that date //*[@id="ContentPlaceHolder1_lblUSD"]
            try:
                all_rates = driver.find_element(By.XPATH, rate_path)                      # //*[@id="ContentPlaceHolder1_lblEUR"]
            except:
                continue
            rate = all_rates.find_element(By.XPATH,"table/tbody/tr/td[3]/span").text # A fx rate
            # rate_en = all_rates[i].find_element(By.XPATH,"table/tbody/tr/td[3]/span").get_attribute("id")[-3:] # FX code, 3 letters
            # rate_mn = all_rates[i].find_element(By.XPATH,"table/tbody/tr/td[2]").text # MN long description of FX code
            print(my_date, rate)
            rates_list.append([my_date,rate])


# export to excel
df = pd.DataFrame(rates_list, columns=['Date', 'MNT_USD'])
df.to_excel('./results/bom_daily_rate.xlsx')
            