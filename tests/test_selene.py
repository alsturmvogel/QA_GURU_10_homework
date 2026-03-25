from selene import be, browser, by


def test_github():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('.FormControl-input').send_keys('eroshenkoam/allure-playwright-example')
    browser.element('.FormControl-input').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-playwright-example')).click()
    browser.element('#issues-tab').click()
    browser.element("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(be.visible)
