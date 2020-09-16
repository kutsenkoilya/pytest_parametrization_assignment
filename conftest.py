
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,help="Choose language")

@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    if user_language is None:
        user_language = 'en'

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print(f"\nstart chrome browser for test with {user_language} profile..")
    browser = webdriver.Chrome(options=options)
    
    yield browser
	
    print("\nquit browser..")
    browser.quit()
