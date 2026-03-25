import allure
from allure_commons.types import Severity
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


def test_dynamic_labels_github_issue():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="GitHub")
    allure.dynamic.label("owner", "eroshenkoam")
    allure.dynamic.title("Проверка Issue через динамические аннотации")

    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-button').click()
        browser.element('.FormControl-input').send_keys('eroshenkoam/allure-playwright-example')
        browser.element('.FormControl-input').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-playwright-example')).click()

    with allure.step('Открываем таб Issue'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с номером 1'):
        browser.element(
            "[href='/eroshenkoam/allure-playwright-example/issues/1']"
        ).should(be.visible)


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может просматривать задачи в репозитории")
@allure.link("https://github.com/eroshenkoam/allure-playwright-example", name="Репозиторий")
@allure.title("Проверка Issue через декораторные аннотации")
def test_decorator_labels_github_issue():
    open_main_page()
    search_repository('eroshenkoam/allure-playwright-example')
    go_repository('eroshenkoam/allure-playwright-example')
    open_issue()
    check_issue('eroshenkoam/allure-playwright-example', 1)
