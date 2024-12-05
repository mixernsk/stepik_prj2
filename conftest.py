import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if not language:
        raise pytest.UsageError("--language parameter is required")

    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {"intl.accept_languages": language})

    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default=None, help="Language for browser"
    )