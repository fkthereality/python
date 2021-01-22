import time
from selene.api import *
from selenium.webdriver import ActionChains
from selene import have, command, be
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.support import select

#browser.config.type_by_js = True
from selene.support.shared import browser
browser.config.hold_browser_open = True
config.browser_name = 'chrome'
config.timeout = 2

def test_basic_case():
    browser.open('http://todomvc4tasj.herokuapp.com/')

    s('[id="new-todo"]').type("a")
    s('[id="new-todo"]').press_enter()

    #browser.element('[id="new-todo"]').type('a').press_enter()
    #browser.element('[d="new-todo"]').perform(command.js.type('a')).press_enter()
        #.should(be.blank)
    #browser.all('[id="todo-list" > li]').should(have.size(1))
    #browser.all('#todo-list>li').should(have.size(1))






# def test_complete_task():
#     # ARRANGE
#     # open TodoMVC page
#     browser.config.hold_browser_open = True
#     browser.open("http://todomvc.com/examples/emberjs/")
#
#     # add tasks: "a", "b", "c"
#     # ACT
#     s('[id="new-todo"]').type("a").press_enter()
#     s('[id="new-todo"]').type("b").press_enter()
#     s('[id="new-todo"]').type("c").press_enter()
#
#     # ASSERT
#     # tasks should be "a", "b", "c"
#     ss('[id="todo-list"] li').should(have.texts('a', 'b', 'c'))
#
#     # toggle b
#     browser.select.select_by_visible_text("b")
#     #s('li [class="ember-view"] input [class="toggle" type="checkbox"]').element('b').click()
#     # completed tasks should be b
#     s(' li [class="completed ember-view"]').should(have.text('b'))
#
#     # active tasks should be a, c
#     ss('[id="todo-list"] li').should(have.texts('a','c'))