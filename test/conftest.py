#  Installation
#  sudo pip install -U pytest
#  sudo pip install selenium


import os
import platform
import pytest
from selenium import webdriver

browsers = {
    'firefox': webdriver.Firefox,
    'chrome':  webdriver.Chrome,
    'ie':      webdriver.Ie
}


@pytest.fixture(scope='session',
                params=browsers.keys())
def webdriver(request):
    if 'DISPLAY' not in os.environ:
        pytest.skip('Test requires display server (export DISPLAY)')

    if request.param == 'ie' and platform.system() != 'Windows':
        pytest.skip('Internet Explorer (IE) only runs in Windows OS')

    if request.param == 'chrome':
        b = browsers[request.param]('/usr/local/webdriver/chromedriver')
    elif request.param == 'ie':
        b = browsers[request.param]('c:\webdriver\IEDriverServer.exe')
    else:
        b = browsers[request.param]()

    request.addfinalizer(b.quit)
    return b


@pytest.fixture
def webbrowser(webdriver, url):
    webdriver.set_window_size(1000, 800)
    webdriver.get(url)
    return webdriver


#
# Note: ONLY single pytest_addoption is needed.  Another pytest_addoption will overwrite this one
#
def pytest_addoption(parser):
    parser.addoption('--url', action='store',
                     default='http://www.python.org')


@pytest.fixture(scope='session')
def url(request):
    return request.config.option.url


# https://www.youtube.com/watch?v=IBC_dxr-4ps

@pytest.fixture(scope='session')
def db_conn():
    return create_db_conn()

@pytest.fixture(scope='module')
def db_table(request, db_conn):
    table = create_table(db_conn, 'foo')
    def fin():
        drop_table(db_conn, table)
    request.addfinalizer(fin)
    return table

def create_db_conn():
    pass

def create_table(db_conn, func):
    pass

def drop_table(db_conn, table):
    pass
