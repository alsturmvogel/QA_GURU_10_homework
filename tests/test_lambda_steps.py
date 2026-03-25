import allure
from selene import be, browser, by


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('.FormControl-input').send_keys('eroshenkoam/allure-playwright-example')
        browser.element('.FormControl-input').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-playwright-example')).click()

    with allure.step('Открываем таб Issure'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issure с номером 1'):
        browser.element("[href='/eroshenkoam/allure-playwright-example/issues/1']").should(be.visible)
