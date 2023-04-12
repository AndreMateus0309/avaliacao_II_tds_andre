import time
from behave import given
from behave import when
from behave import then
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'login no sistema')
def step_impl(context):
    url_site = "https://luvas01rc.com/"
    context.driver.get(url_site)
    #raise NotImplementedError(u'STEP: Given login no sistema')


@given(u'ter clicado no botao Loja')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="menu-item-11886"]/a/span'))).click()
    #raise NotImplementedError(u'STEP: Given ter clicado no botao Loja')


@then(u'deve-se navegar pela loja, vendo diferentes modelos de luvas')
def step_impl(context):
    pyautogui.moveTo(1850, 700, duration=2)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.vscroll(1, -200)
    pyautogui.moveTo(1850, 300, duration=3)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.vscroll(1, 100)
    #raise NotImplementedError(u'STEP: Then deve-se navegar pela loja, vendo diferentes modelos de luvas')