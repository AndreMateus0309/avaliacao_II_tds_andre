from bs4 import BeautifulSoup
import time
from behave import given
from behave import when
from behave import then
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'ter entrado na Loja')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-11886"]/a/span'))).click()
    #raise NotImplementedError(u'STEP: Given ter entrado na Loja')


@then(u'deve-se navegar pela loja, vendo diferentes modelos de luvas, e retirando dados das mesmas')
def step_impl(context):
    pyautogui.moveTo(1800, 700, duration=2)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.vscroll(1, -200)
    pyautogui.moveTo(1800, 300, duration=3)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.vscroll(1, 100)
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/article/ul/li[1]/div/ul/li[6]/a'))).click()
    pyautogui.moveTo(1800, 300, duration=3)
    pyautogui.click()
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-11845"]/div[3]/div[1]/p'))).click()
    aux = context.driver.find_element(By.XPATH, '//*[@id="product-11845"]/div[3]/div[1]/p')
    content = aux.get_attribute('outerHTML')
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.find(name='p')

    with open('file.html', 'w') as sample:
        sample.write(str(text))
    sample.close()

    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-11845"]/div[1]/ul/li[2]/a[2]/i'))).click()
    aux = context.driver.find_element(By.XPATH, '//*[@id="product-11844"]/div[3]/div[1]/p')
    content = aux.get_attribute('outerHTML')
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.find(name='p')

    with open('file.html', 'w') as sample:
        sample.write(str(text))
    sample.close()
    #raise NotImplementedError(u'STEP: Then deve-se navegar pela loja, vendo diferentes modelos de luvas, e retirando dados das mesmas (cores, tamanho, preços, detalhes)')