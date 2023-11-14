import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from dotenv import load_dotenv

load_dotenv()

# chrome stays open
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url="https://tinder.com/app/recs")

try:

    login = driver.find_element(by=By.CSS_SELECTOR, value="a.c1p6lbu0")
    login.click()

    time.sleep(5)
    login_with_fb = driver.find_element(by=By.XPATH, value='//*[@id="o557388692"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button')
    login_with_fb.click()

    time.sleep(2)

    # because tinder is logged in with new pop up window facebook,
    # we need selenium window_handles
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]

    # switch to facebook window
    driver.switch_to.window(fb_login_window)
    print(driver.title)

    fb_email = driver.find_element(by=By.NAME, value="email")
    fb_email.send_keys(os.environ.get("EMAIL"))

    fb_pass = driver.find_element(by=By.NAME, value="pass")
    fb_pass.send_keys(os.environ.get("PASS"))
    fb_pass.send_keys(Keys.ENTER)

    time.sleep(10)
    receive_code_link = driver.find_element(by=By.CSS_SELECTOR, value="#checkpointBottomBar a")
    receive_code_link.click()

    time.sleep(2)
    send_login_code = driver.find_element(by=By.CSS_SELECTOR, value="div._4ucb a")
    send_login_code.click()

    time.sleep(1)
    close_modal = driver.find_element(by=By.CSS_SELECTOR, value="div.clearfix a._42ft")
    close_modal.click()

    # please change this time according to your needs
    # sometimes sms token delays and you need more than 20 seconds
    # to input it manually
    time.sleep(20)
    send_login_code = driver.find_element(by=By.CSS_SELECTOR, value="#checkpointBottomBar button")
    send_login_code.click()

    submit_continue_to_tinder = driver.find_element(by=By.XPATH, value='//*[@id="checkpointSubmitButton"]')
    submit_continue_to_tinder.click()

except NoSuchElementException as e:
    print(str(e))

except ElementNotInteractableException as e:
    print(str(e))
