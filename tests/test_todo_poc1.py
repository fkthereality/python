import time

from selene import have
from selene.api import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser.config.hold_browser_open = True
browser.config.timeout = 15
browser.config.type_by_js = False


def test_basic_case():
    browser.open('http://todomvc4tasj.herokuapp.com/')
    browser.element('#new-todo').type('a')
    time.sleep(3)
    ActionChains(browser.driver()) \
        .key_down(Keys.ENTER) \
        .key_up(Keys.ENTER) \
        .perform()
    time.sleep(3)
    browser.element('#new-todo').should(be.blank)
    browser.all('#todo-list>li')[0].should(have.exact_text('a'))
    browser.all('#todo-list>li').should(have.size(1))
