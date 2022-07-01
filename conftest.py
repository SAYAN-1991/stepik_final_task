import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, en-gb, ru, fr, de, es, it, sk, pt")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language in ("en", "en-gb", "ru", "fr", "de", "es", "it", "sk", "pt"):
        print("\nstart chrome browser for test language = " + user_language)
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be en, en-gb, ru, fr, de, es, it, sk, pt")
    yield browser
    print("\nquit browser..")
    browser.quit()

#pytest -v --tb=line --language=en test_main_page.py
#pytest -v --tb=line --language=en-gb test_main_page.py
