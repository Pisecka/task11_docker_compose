import pytest
import os
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--b_version", default="99.0")
    parser.addoption("--url", default="https://demo.opencart.com/")


@pytest.fixture(scope="session", autouse=True)
def get_environment(request, pytestconfig):
    props = {
        'Browser': request.config.getoption("--browser"),
        'Browser.Version': request.config.getoption("--b_version"),
        'Shell': os.getenv('SHELL')
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
        env_props = '\n'.join([f'{k}={v}' for k, v in props.items()])
        f.write(env_props)


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    b_version = request.config.getoption("--b_version")
    url = request.config.getoption("--url")

    executor_url = f"http://selenoid:4444/wd/hub"
    caps = {
        "browserName": browser,
        "browserVersion": b_version,
        "screenResolution": "1280x720",
        "name": "Karina",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False,
            #     "enableLog": logs
        },
        # 'acceptSslCerts': True,
        # 'acceptInsecureCerts': True,
        # 'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {}
    }

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=caps
    )

    # set base_url as attribute
    driver.url = url

    # set time - 5 sec
    driver.t = 5

    driver.maximize_window()
    driver.get(url)
    request.addfinalizer(driver.quit)
    return driver
