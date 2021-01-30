from selene.api import *
# config.hold_browser_open = True


def test_add_toggle_todos():
    browser.open_url('https://todomvc.com/examples/emberjs/')
    browser.element('#new-todo').type('a').press_enter()
    browser.element('#new-todo').type('b').press_enter()
    browser.element('#new-todo').type('c').press_enter()
    browser.elements("label").should(have.exact_texts('a', 'b', 'c'))
    browser.all('#todo-list>li').element_by(have.exact_text('b')) \
        .element('.toggle').click()
    browser.element('.completed').should(have.exact_text('b'))
    browser.open_url('https://todomvc.com/examples/emberjs/#/active')
    browser.elements("label").should(have.exact_texts('a', 'c'))
