from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


# ARRANGE
def test_search():
    browser.open("https://www.ecosia.org/")

    # ACT
    s('input').type("yashaka selene").press_enter()
    s('a.result-title').click()

    # ASSERT
    ss('[href="/yashaka/selene"]').should(have.size(3))
    return test_search
