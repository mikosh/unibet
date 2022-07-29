from seleniumbase import BaseCase
from time import sleep


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://www.google.com/")
        self.save_screenshot_to_logs()
        sleep(3)