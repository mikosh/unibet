from seleniumbase import BaseCase
from time import sleep


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://www.google.com/")
        self.click("button#L2AGLb div")
        self.type('input[name="q"]', "test")
        self.click("body div:nth-of-type(3) form div")
        self.click("body div:nth-of-type(3) form div div:nth-of-type(3) center input")
        self.open("https://www.google.com/search?q=test")
        sleep(3)