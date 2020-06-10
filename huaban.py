from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.huaban.com/')
wait = WebDriverWait(driver,3) # 等待3S

widget_input = driver.find_element_by_xpath('//*[@id="query"]')
widget_input.send_keys('李宣美')
#输入回车
widget_input.send_keys(Keys.ENTER)

wait = WebDriverWait(driver,5) # 等待5s 图片加载

widget_image_list = driver.find_element_by_xpath('//*[@id="waterfall"]')

widget_image_items = driver.find_elements_by_xpath('//*[@id="waterfall"]/div/a')


for i in widget_image_items:
    # print('i=',i)
    current_window = driver.current_window_handle  # 获取当前窗口handle name
    driver.execute_script("arguments[0].click();", i)
    sleep(2)
    all_window = driver.window_handles
    for window in all_window:
        if window != current_window:
            driver.switch_to.window(window)
    try:
        widget_big_image_element = driver.find_element_by_xpath('//*[@id="baidu_image_holder"]/img')
    except:
        widget_big_image_element = driver.find_element_by_xpath('// *[ @ id = "baidu_image_holder"] / a / img')
    finally:
        widget_big_image = widget_big_image_element.get_attribute('src')

    print('widget_big_image=',widget_big_image)
    driver.back()

