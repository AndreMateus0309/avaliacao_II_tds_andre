from selenium import webdriver
import time as t

def before_all(context):
    t.sleep(2)
    print("Começou o teste")
    t.sleep(5)
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    context.driver = webdriver.Chrome(options = options)
    context.driver.maximize_window()

def before_scenario(context, scenario):
    context.driver.implicitly_wait(5)

def after_scenario(context, step):
    print("Acabou o cenario!")
    t.sleep(2)
    print("Preparando para o proximo")

def after_all(context):
    context.driver.quit()
    t.sleep(3)
    print("Teste finalizado com sucesso!")
