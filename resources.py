from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from robot.api import logger
import time
import jwt

injection = {'SQL injection (intro)': '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[5]/ul[1]/li[1]/a[1]',
             'SQL injection (advanced)': '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[5]/ul[1]/li[2]/a[1]',
             'SQL injection (mitigation)': '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[5]/ul[1]/li[3]/a[1]'}


def register_user(username, password):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://127.0.0.1:8080/WebGoat/login')
    time.sleep(1)
    register_link = driver.find_element(By.XPATH,
                                        '/html[1]/body[1]/section[1]/section[1]/section[1]/form[1]/div[3]/a[1]')
    register_link.click()
    username_field = driver.find_element(By.XPATH,
                                         '/html[1]/body[1]/section[1]/section[1]/section[1]/fieldset[1]/form[1]/div['
                                         '1]/div[1]/input[1]')
    password_field = driver.find_element(By.XPATH,
                                         '/html[1]/body[1]/section[1]/section[1]/section[1]/fieldset[1]/form[1]/div[2]'
                                         '/div[1]/input[1]')
    confirm_password_field = driver.find_element(By.XPATH,
                                                 '/html[1]/body[1]/section[1]/section[1]/section[1]/fieldset[1]/form[1]'
                                                 '/div[3]/div[1]/input[1]')
    username_field.send_keys(username)
    password_field.send_keys(password)
    confirm_password_field.send_keys(password)
    agree_tick = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/fieldset[1]/form[1]'
                                               '/div[5]/div[1]/div[1]/label[1]/input[1]')
    agree_tick.click()
    submit_button = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/fieldset[1]/'
                                                  'form[1]/div[6]/div[1]/button[1]')
    submit_button.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[6]/div[3]/div[1]/'
                                                                                'h2[1]')))
    driver.quit()


def login(username, password):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://127.0.0.1:8080/WebGoat/login')
    time.sleep(1)
    username_field = driver.find_element(By.XPATH,
                                         '/html[1]/body[1]/section[1]/section[1]/section[1]/form[1]/div[1]/input[1]')
    password_field = driver.find_element(By.XPATH,
                                         '/html[1]/body[1]/section[1]/section[1]/section[1]/form[1]/div[2]/input[1]')
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/form[1]/button[1]')
    login_button.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/'
                                                                                'div[1]/ul[1]/li[1]/a[1]')))
    return driver


def close_window(driver):
    driver.quit()


def switch_to_injection(driver):
    injection_field = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[5]/a[1]')
    injection_field.click()
    return driver


def what_is_sql(driver):
    intro = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[5]/ul[1]/li[1]/a[1]')
    intro.click()
    box2 = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/'
                                         'div[1]/div[1]/div[5]/div[1]/div[1]/a[2]/div[1]')
    box2.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]'
                                                                                '/div[1]/div[1]/div[6]/div[4]/div[2]/'
                                                                                'form[1]/table[1]/tbody[1]/tr[1]/'
                                                                                'td[2]/input[1]')))
    sql_query = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]'
                                              '/div[1]/div[1]/div[6]/div[4]/div[2]/form[1]/table[1]/tbody[1]/tr[1]/'
                                              'td[2]/input[1]')
    sql_query.send_keys("SELECT department FROM employees WHERE first_name='Bob' AND last_name='Franco'")
    submit_button = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                  'div[1]/div[1]/div[1]/div[6]/div[4]/div[2]/form[1]/table[1]/tbody[1]'
                                                  '/tr[2]/td[1]/button[1]')
    submit_button.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,
                                                                      "//div[normalize-space()="
                                                                      "'You have succeeded!']")))
    outcome = driver.find_element(By.XPATH, "//div[normalize-space()='You have succeeded!']").text
    return outcome


def data_manipulation_language(driver):
    intro = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[5]/ul[1]/li[1]/a[1]')
    intro.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[5]/div[1]/div[1]/'
                                                                                'a[3]/div[1]')))
    box3 = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/'
                                         'div[1]/div[1]/div[5]/div[1]/div[1]/a[3]/div[1]')
    box3.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[6]/div[5]/div[3]/'
                                                                                'form[1]/table[1]/tbody[1]/tr[1]/td[2]'
                                                                                '/input[1]')))
    sql_query = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]'
                                              '/div[1]/div[1]/div[6]/div[5]/div[3]/form[1]/table[1]/tbody[1]/tr[1]/'
                                              'td[2]/input[1]')
    sql_query.send_keys("UPDATE employees SET department='Sales' WHERE first_name='Tobi'")
    submit_button = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                  'div[1]/div[1]/div[1]/div[6]/div[5]/div[3]/form[1]/table[1]/'
                                                  'tbody[1]/tr[2]/td[1]/button[1]')
    submit_button.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//div[normalize-space()="
                                                                                "'Congratulations. You have "
                                                                                "successfully completed the assignment."
                                                                                "']")))
    outcome = driver.find_element(By.XPATH, "//div[normalize-space()='Congratulations. You have successfully "
                                            "completed the assignment.']").text
    return outcome


def data_definition_language(driver):
    intro = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[5]/ul[1]/li[1]/a[1]')
    intro.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[5]/div[1]/div[1]/'
                                                                                'a[3]/div[1]')))
    box4 = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/'
                                         'div[1]/div[1]/div[5]/div[1]/div[1]/a[4]/div[1]')
    box4.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[6]/div[6]/div[2]/'
                                                                                'form[1]/table[1]/tbody[1]/tr[1]/'
                                                                                'td[2]/input[1]')))
    sql_query = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]'
                                              '/div[1]/div[1]/div[6]/div[6]/div[2]/form[1]/table[1]/tbody[1]/'
                                              'tr[1]/td[2]/input[1]')
    sql_query.send_keys("ALTER TABLE employees ADD phone varchar(20)")
    submit_button = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                  'div[1]/div[1]/div[1]/div[6]/div[6]/div[2]/form[1]/table[1]/tbody[1]'
                                                  '/tr[2]/td[1]/button[1]')
    submit_button.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/section[1]/section[1]"
                                                                                "/section[1]/div[1]/div[1]/div[1]/"
                                                                                "div[1]/div[1]/div[6]/div[6]/div[2]/"
                                                                                "div[2]")))
    outcome = driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/"
                                            "div[1]/div[1]/div[6]/div[6]/div[2]/div[2]").text
    return outcome


def data_control_language(driver):
    intro = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[5]/ul[1]/li[1]/a[1]')
    intro.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[5]/div[1]/div[1]/'
                                                                                'a[5]/div[1]')))
    box5 = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/'
                                         'div[1]/div[1]/div[5]/div[1]/div[1]/a[5]/div[1]')
    box5.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[6]/div[7]/div[2]/'
                                                                                'form[1]/table[1]/tbody[1]/tr[1]/td[2]'
                                                                                '/input[1]')))
    sql_query = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]'
                                              '/div[1]/div[1]/div[6]/div[7]/div[2]/form[1]/table[1]/tbody[1]/tr[1]/'
                                              'td[2]/input[1]')
    sql_query.send_keys("GRANT all ON grant_rights TO unauthorized_user")
    submit_button = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                  'div[1]/div[1]/div[1]/div[6]/div[7]/div[2]/form[1]/table[1]/tbody[1]'
                                                  '/tr[2]/td[1]/button[1]')
    submit_button.click()

    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/section[1]/section[1]"
                                                                                "/section[1]/div[1]/div[1]/div[1]/"
                                                                                "div[1]/div[1]/div[6]/div[7]/div[2]/"
                                                                                "div[2]")))
    outcome = driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/"
                                            "div[1]/div[1]/div[6]/div[7]/div[2]/div[2]").text
    return outcome


def switch_to_cryptographic_failures(driver):
    cryptographic_field = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]'
                                                        '/li[4]/a[1]/span[1]')
    cryptographic_field.click()
    return driver


def private_key(driver):
    crypto_basics = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/'
                                                  'li[4]/ul[1]/li[1]/a[1]')
    crypto_basics.click()
    time.sleep(5)
    box6 = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/div[1]'
                                         '/div[1]/div[5]/div[1]/div[1]/a[6]/div[1]')
    box6.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[6]/div[8]/div[8]/'
                                                                                'pre[1]/div[1]')))
    key = driver.find_element(By.XPATH, "//div[@id='privatekey']").text
    return key


def paste_response(driver, modulus, signature):
    modulus_box = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                'div[1]/div[1]/div[1]/div[6]/div[8]/div[8]/form[1]/input[1]')
    signature_box = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                  'div[1]/div[1]/div[1]/div[6]/div[8]/div[8]/form[1]/input[2]')
    modulus_box.send_keys(modulus)
    signature_box.send_keys(signature)
    post_the_answer = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                    'div[1]/div[1]/div[1]/div[6]/div[8]/div[8]/form[1]/input[3]')
    post_the_answer.click()
    outcome = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                            'div[1]/div[1]/div[1]/div[6]/div[8]/div[8]/div[2]').text
    return outcome


def encoding_base64(driver):
    crypto_basics = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/'
                                                  'li[4]/ul[1]/li[1]/a[1]')
    crypto_basics.click()
    time.sleep(5)
    box2 = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/div[1]'
                                         '/div[1]/div[5]/div[1]/div[1]/a[2]/div[1]')
    box2.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[6]/div[4]/div[1]/'
                                                                                'div[1]/div[5]/div[4]/div[1]/pre[1]')))
    base = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]'
                                         '/div[1]/div[1]/div[6]/div[4]/div[2]/div[2]').text
    return base


def paste_decoded(driver, username, password):
    username_box = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                 'div[1]/div[1]/div[1]/div[6]/div[4]/div[2]/form[1]/input[1]')
    password_box = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                 'div[1]/div[1]/div[1]/div[6]/div[4]/div[2]/form[1]/input[2]')
    username_box.send_keys(username)
    password_box.send_keys(password)
    post_the_answer = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]'
                                                    '/div[1]/div[1]/div[1]/div[6]/div[4]/div[2]/form[1]/input[3]')
    post_the_answer.click()
    outcome = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/'
                                            'div[1]/div[1]/div[6]/div[4]/div[2]/div[3]').text
    return outcome


def switch_to_identity_auth_failure(driver):
    cryptographic_field = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/aside[1]/div[1]/ul[1]/li[8]/a[1]'
                                                        '/span[1]')
    cryptographic_field.click()
    return driver


def how_long(driver):
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//a[@id='A7IdentityAuthFailure"
                                                                                "-SecurePasswords']")))
    intro = driver.find_element(By.XPATH, "//a[@id='A7IdentityAuthFailure-SecurePasswords']")
    intro.click()
    time.sleep(5)
    box4 = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/'
                                         'div[1]/div[1]/div[5]/div[1]/div[1]/a[4]/div[1]')
    box4.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '/html[1]/body[1]/section[1]/section[1]'
                                                                                '/section[1]/div[1]/div[1]/div[1]/'
                                                                                'div[1]/div[1]/div[6]/div[6]/div[2]/'
                                                                                'form[1]/div[1]/input[1]')))
    password = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]'
                                             '/div[1]/div[1]/div[6]/div[6]/div[2]/form[1]/div[1]/input[1]')
    password.send_keys("Zaluzje12#$")
    submit_button = driver.find_element(By.XPATH, '/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/'
                                                  'div[1]/div[1]/div[1]/div[6]/div[6]/div[2]/form[1]/div[2]/button[1]')
    submit_button.click()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "/html[1]/body[1]/section[1]/section[1]"
                                                                                "/section[1]/div[1]/div[1]/div[1]/"
                                                                                "div[1]/div[1]/div[6]/div[6]/"
                                                                                "div[2]/div[2]")))
    outcome = driver.find_element(By.XPATH, "/html[1]/body[1]/section[1]/section[1]/section[1]/div[1]/div[1]/div[1]/"
                                            "div[1]/div[1]/div[6]/div[6]/div[2]/div[2]").text
    return outcome
