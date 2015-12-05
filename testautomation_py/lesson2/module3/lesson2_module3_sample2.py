import smtpd
import asyncore
import random
import sys
import threading
import time
import pytest

from selenium import webdriver


class FakeSMTPServer(smtpd.SMTPServer, threading.Thread):

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self)
        smtpd.SMTPServer.__init__(self, *args, **kwargs)
        self.daemon = True
        self.received_messages = []
        self.start()

    def run(self):
        asyncore.loop()

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        self.received_messages.append(data)

    def reset(self):
        self.received_messages = []

    def wait_for_mail(self, timeout):
        end_time = time.time() + timeout
        while True:
            if len(self.received_messages) > 0:
                return
            time.sleep(1)
            if time.time() > end_time:
                assert False


@pytest.fixture
def smtp_server(request):
    server = FakeSMTPServer(('localhost', 25), None)
    request.addfinalizer(lambda: server.close())
    return server


@pytest.fixture
def browser(request):
    driver = webdriver.Firefox()
    request.addfinalizer(lambda: driver.quit())
    return driver


def test_mail(smtp_server, browser):
    testuser = 'testuser_%s' % random.randint(0, sys.maxsize)

    browser.get('http://localhost/mantisbt-1.2.19/signup_page.php')
    browser.find_element_by_name('username').send_keys(testuser)
    browser.find_element_by_name('email').send_keys('%s@localhost' % testuser)
    browser.find_element_by_css_selector('input[type=submit]').click()

    smtp_server.wait_for_mail(10)
    assert len(smtp_server.received_messages) == 2
