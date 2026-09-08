import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option('detach',True)
options.set_capability("browserName","chrome")

path = "D:\webdriver\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=path)
driver = webdriver.Chrome(options,service)

# driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

while True:

    # 1、点击百度首页搜索框下面的6个链接，从1至6分别点击
    n = 6
    for i in range(1, n + 1):
        time.sleep(2)
        # 点击链接的A标签地址
        a_xpath = f'//*[@id="hotsearch-content-wrapper"]/li[{i}]/a'
        print(a_xpath)
        driver.find_element(By.XPATH, a_xpath).click()

        time.sleep(2)

        # 获取所有打开的窗口的句柄
        window_handles = driver.window_handles
        # 切换到最新打开的窗口
        driver.switch_to.window(window_handles[1])

        for ii in range(3):
            driver.execute_script("window.scrollBy(0,350)")
            time.sleep(1)

        for ii in range(3):
            driver.execute_script("window.scrollBy(0,-350)")
            time.sleep(1)

        nn = 3
        for a in range(2, nn+1):
            aa_xpath = f'//*[@id="1"]/div/div/div/div[1]/div/div/div[2]/div[1]/h3/a/div/div/p/span/span'
            print(aa_xpath)
            driver.find_element(By.XPATH, aa_xpath).click()

            # 获取所有打开的窗口的句柄
            window_handles = driver.window_handles
            # 切换到最新打开的窗口
            driver.switch_to.window(window_handles[2])

            for iii in range(5):
                driver.execute_script("window.scrollBy(0,350)")
                time.sleep(1)

            time.sleep(1)
            # 关闭新打开的窗口
            driver.close()

            window_handles = driver.window_handles
            # 切换到最新打开的窗口
            driver.switch_to.window(window_handles[1])
            time.sleep(2)

        time.sleep(2)

        # 获取所有打开的窗口的句柄
        window_handles = driver.window_handles
        # 切换到最新打开的窗口
        driver.switch_to.window(window_handles[1])
        # 关闭新打开的窗口
        driver.close()

        # 获取所有打开的窗口的句柄
        window_handles = driver.window_handles

        # 切换到第一个打开的窗口
        driver.switch_to.window(window_handles[0])

    driver.find_element(By.XPATH, '//*[@id="hotsearch-refresh-btn"]/span').click()

