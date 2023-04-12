from behave import given
from behave import then
from behave import when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@then(u'deve-se abrir o sistema da loja de luvas da 01RC')
def step_impl(context):
    url_site = "https://luvas01rc.com/"
    context.driver.get(url_site)
    #raise NotImplementedError(u'STEP: Then deve-se abrir o sistema da loja de luvas da 01RC')