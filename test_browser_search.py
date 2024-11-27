from selene import browser, be, have


def test_successful_search(setting_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Tests with Selene'))

def test_failed_search(setting_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="footcnt"]').should(have.text('This text cannot exist'))
