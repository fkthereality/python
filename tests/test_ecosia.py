from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene.support.shared.jquery_style import ss


def test_search():
    # ARRANGE
    browser.open("https://www.ecosia.org/")

    # ACT
    s('[name="q"]').type("yashaka selene").press_enter()
    s('a.result-title').click()

    # ASSERT
    ss('[href="/yashaka/selene"]').should(have.size(3))
