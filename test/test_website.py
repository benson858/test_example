#
# http://selenium-python.readthedocs.org/getting-started.html
#

import pytest
from selenium.webdriver.common.keys import Keys


# py.test test_website.py  ;;default is http://www.python.org
# py.test test_website.py  --url=http://www.google.com/xhtml;
#
def test_website_title(webbrowser):
    print "url=%s" % webbrowser.current_url
    assert "Python" in webbrowser.title
    elem = webbrowser.find_element_by_name("q")          ## OR use webbrowser.find_element_by_xpath('//*[@id="id-search-field"]')
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)                          ## OR elem.submit()  will work too
    assert "No results found." not in webbrowser.page_source


def xxxtest_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def xxxtest_python_website_title(webdriver):
    webdriver.get('http://www.python.org')
    assert "Python" in webdriver.title

def xxxtest_pytest_website_title(webdriver):
    webdriver.get('https://pytest.org/latest')
    assert 'pytest' in webdriver.title

