from seleniumbase import BaseCase
from time import sleep


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://www.google.com/")
        sleep(3)