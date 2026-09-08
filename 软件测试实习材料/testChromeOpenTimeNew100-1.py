from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import unittest

import logging

# 创建一个logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)  # 设置日志级别

# 创建一个handler，用于将日志写入磁盘文件
file_handler = logging.FileHandler('testChromeOpenTimeNew100-1.log', mode='w')
file_handler.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# 将handlers添加到logger
logger.addHandler(file_handler)

# 定义一个全局变量
a = 1
path = ""


class TestChromeOpenTime(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test01_baidu(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.baidu.com/"]
        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址a次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)

                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, "bottom_layer")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test02_qq(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.qq.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)

                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, "qqhome-china-medal")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test03_sohu(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.sohu.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "entrance")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test04_sina(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.sina.com.cn/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="wwwidx_imp_con"]/div[1]')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test05_163(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.163.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True
            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, 'mod_news_tab')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test06_eastmoney(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://eastmoney.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "emsider_backtop_t")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test07_so(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.so.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="input"]')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test08_csdn(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.csdn.net/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="floor-www-index_558"]/div/div[4]/div/div[1]/div/ul/li[7]/a')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test09_sogou(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.sogou.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'stb')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test10_bilibili(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.bilibili.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[3]/div[2]/div[2]/a[2]/span')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test11_zhihu(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.zhihu.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "SignFlowHomepage-logo")))
                    print(element.id)

                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test12_douban(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.douban.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "anony-sns")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test13_zol(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.zol.com.cn/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "text")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test14_1688(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.1688.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                        (By.NAME, 'keywords')))
                    print(element.id)

                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test15_blog_csdn(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://blog.csdn.net/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'blog-nav-box')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test16_movie_douban(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://movie.douban.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="content"]/div/div[2]/div[3]/div[2]/h2/div[1]')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test17_zhuanlan_zhihu(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://zhuanlan.zhihu.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "ColumnHomeBottom-footer")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test18_jd(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.jd.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'elevator_lk_txt')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test19_ifeng(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.ifeng.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[6]/div[3]/div[1]')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test20_iqiyi(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.iqiyi.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()


                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "simple-buttons_iqiyiLogo__gPDgC")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test21_pcauto(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.pcauto.com.cn/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "JtsearchForm")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test22_2345(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.2345.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'famous-web')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test23_chinaz(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.chinaz.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="cz"]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]')))
                    print(element.id)

                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test24_qidian(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://qidian.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # 有安全验证网站增加此行代码
                options.add_argument("--disable-blink-features=AutomationControlled")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, 'rank-list-row')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test25_ali213(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.ali213.net/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()


                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[15]/span')))
                    print(element.id)

                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test26_58(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://58.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()


                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="popular-services"]/h2/a')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test27_ctrip(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://ctrip.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "hs_search-btn-container_R0HuJ")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test28_ip138(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://ip138.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()


                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "mobile")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test29_weibo(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://weibo.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()


                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "app")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test30_pconline(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.pconline.com.cn/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="Jarea-p2"]/div/div[2]/div[2]/div[1]')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test31_autohome(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.autohome.com.cn/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)

                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.ID, "searchIpt")))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test32_bendibao(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.bendibao.com//"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'wd')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test33_39(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.39.net/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'yyksearch')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test34_hupu(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.hupu.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")
                options.add_argument("--disable-blink-features=AutomationControlled")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div/div[2]/div/div[1]/div[1]/div')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test35_china(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["http://www.china.com.cn/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/ul/li[2]')))
                    print(element.id)

                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test36_ximalaya(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.ximalaya.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="jymain"]/div[1]/div[3]/div[2]/div[3]/ol[1]')))
                    print(element.id)

                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test37_66law(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.66law.cn/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="ad_onlin"]/div/div[1]')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test38_3dmgame(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.3dmgame.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'keyword')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test39_dict(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://dict.cn/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)

                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="idxRightBan"]/div[2]/a')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test40_kugou(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.kugou.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/a/img')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test41_tianqi(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.tianqi.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="main_map"]/div[1]/canvas')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test42_tianqi(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.onlinedown.net/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'week-rec')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test43_51test(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.51test.net/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'col-md')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test44_apple(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.apple.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 20).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="globalnav-list"]/li[1]/a')))
                    print(element.id)

                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test45_anjuke(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.anjuke.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'search-input')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test46_bing(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.bing.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'sb_form_q')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test47_zdic(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.zdic.net/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'q')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test48_cncn(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://www.cncn.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'so_input')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test49_book_qq(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://book.qq.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'searchSubmit')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")

    def test50_mp_weixin_qq(self):

        # 定义一个列表，存储要测试的网址
        url_list = ["https://mp.weixin.qq.com/"]

        # 遍历列表中的每个网址
        for url in url_list:
            # 定义一个变量，用来存储初始的时间
            total_load_time = 0
            error_info = True

            # 重复打开同一个网址100次
            for i in range(a):
                # 创建一个新的Chrome浏览器对象，为了公平测算，每访问一个url都重置下浏览器对象，让其没有缓存影响，
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                options.add_argument("disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_experimental_option('detach', True)
                options.set_capability("browserName", "chrome")

                # path = "C:\webdriver脚本\chromedriver-win64\chromedriver.exe"
                service = Service(executable_path=path)
                self.driver = webdriver.Chrome(options, service)

                # 记录开始的时间戳
                start_time = time.time()

                try:
                    # 打开网址
                    self.driver.get(url)
                    element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div/div[2]/div[2]/div[1]/div/dl/dt/span')))
                    print(element.id)
                except Exception as e:
                    # 处理所有异常
                    print(f"发生异常：{e}")
                    error_info = False
                    break

                finally:

                    end_time = time.time()
                    load_time = end_time - start_time
                    total_load_time += load_time
                    # 关闭浏览器对象
                    self.driver.quit()

            # 计算平均加载时间，单位为秒
            average_load_time = total_load_time / a

            # 打印平均加载时间
            if error_info:
                logger.info(f"{url}的平均加载时间为{average_load_time}秒")
            else:
                logger.info(f"{url}的发生异常")


if __name__ == '__main__':
    unittest.main()
