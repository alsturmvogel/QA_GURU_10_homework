import allure
from selene import be, browser, by


def test_decorator_steps():
    open_main_page()
    search_repository('eroshenkoam/allure-playwright-example')
    go_repository('eroshenkoam/allure-playwright-example')
    open_issue()
    check_issue('eroshenkoam/allure-playwright-example', 1)


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('.FormControl-input').send_keys(repo)
    browser.element('.FormControl-input').press_enter()


@allure.step('Переходим по ссылке репозитория')
def go_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб Issue')
def open_issue():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие Issure с номером 1')
def check_issue(repo, number):
    browser.element(f"[href='/{repo}/issues/{number}']").should(be.visible)
