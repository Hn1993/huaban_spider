from random import random
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import requests



driver = webdriver.Chrome()

#  在这里加一个获取代理ip的方法
# driver.get('https://www.xicidaili.com/nn')  # 西刺代理
#
# # 如果  xpath为 下一页  的元素可见，执行下一步  否则，等待最长的10S的等待时间
# WebDriverWait(driver,10).until(EC.visibility_of(driver.find_element_by_xpath('//*[@id="body"]/div[3]/a[11]')))
# random_num = random.randint(2,98)
# print('random_num=',random_num)
# random_proxy_ip_info = driver.find_element_by_xpath('//*[@id="ip_list"]/tbody/tr['+str(random_num)+']')
# random_proxy_ip_info_list = str(random_proxy_ip_info.text).replace('\n', ' ').replace('\r', ' ').split(' ')
# print('ip=',random_proxy_ip_info_list[0])
# print('port=',random_proxy_ip_info_list[1])
# print('type=',random_proxy_ip_info_list[4])
# driver.close()
#
# proxy_ip = str(random_proxy_ip_info_list[4])+"://"+str(random_proxy_ip_info_list[0])+":"+str(random_proxy_ip_info_list[1])
# chromeOptions = webdriver.ChromeOptions()
# # 设置代理
# chromeOptions.add_argument('--proxy-server='+str)
# # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
# driver = webdriver.Chrome(options = chromeOptions)



driver.get('https://www.huaban.com/')
wait = WebDriverWait(driver,3) # 等待3S

widget_input = driver.find_element_by_xpath('//*[@id="query"]')
widget_input.send_keys('李宣美')
#输入回车
widget_input.send_keys(Keys.ENTER)

wait = WebDriverWait(driver,10) # 等待5s 图片加载

widget_image_list = driver.find_element_by_xpath('//*[@id="waterfall"]')

widget_image_items = driver.find_elements_by_xpath('//*[@id="waterfall"]/div/a')

current_window = driver.current_window_handle  # 获取当前窗口handle name
driver.execute_script("arguments[0].click();", widget_image_items[0])
all_window = driver.window_handles
for window in all_window:
    if window != current_window:
        driver.switch_to.window(window)
sleep(2)

for i in range(50):
    widget_next_page = driver.find_element_by_xpath('//*[@id="pin_view_layer"]/div[3]/a[1]')
    driver.execute_script("arguments[0].click();", widget_next_page)
    sleep(1)
    try:
        widget_big_image_element = driver.find_element_by_xpath('//*[@id="baidu_image_holder"]/img')
    except:
        widget_big_image_element = driver.find_element_by_xpath('// *[ @ id = "baidu_image_holder"] / a / img')
    finally:
        widget_big_image = widget_big_image_element.get_attribute('src')
    print('widget_big_image=', widget_big_image)
    with open("E:\\Coding\\pyProject\\webClick\\huabanImage\\"+str(i)+".jpg", 'wb')as jpg:
        jpg.write(requests.get(widget_big_image).content)




# for i in widget_image_items:
#     # print('i=',i)
#     current_window = driver.current_window_handle  # 获取当前窗口handle name
#     driver.execute_script("arguments[0].click();", i)
#     sleep(2)
#     all_window = driver.window_handles
#     for window in all_window:
#         if window != current_window:
#             driver.switch_to.window(window)
#     try:
#         widget_big_image_element = driver.find_element_by_xpath('//*[@id="baidu_image_holder"]/img')
#     except:
#         widget_big_image_element = driver.find_element_by_xpath('// *[ @ id = "baidu_image_holder"] / a / img')
#     finally:
#         widget_big_image = widget_big_image_element.get_attribute('src')
#
#     print('widget_big_image=',widget_big_image)
#     driver.back()

