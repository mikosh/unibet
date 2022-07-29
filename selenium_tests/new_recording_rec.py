from seleniumbase import BaseCase
from time import sleep


class RecorderTests(BaseCase):
    def test_recording(self):
        self.open("https://www.google.com/")
        self.click("button#L2AGLb div")
        sleep(3)
        self.type('input[name="q"]', "test")
        self.click("body div:nth-of-type(3) form div")
        self.click("body div:nth-of-type(3) form div div:nth-of-type(3) center input")
        self.open("https://www.google.com/search?q=test&source=hp&ei=8ZHiYpb7KNK8xc8PtpSe4AI&iflsig=AJiK0e8AAAAAYuKgAZvuWlFjukh4b3PSeRPzqF99zRSB&ved=0ahUKEwjWt7f72pv5AhVSXvEDHTaKBywQ4dUDCAs&oq=test&gs_lcp=Cgdnd3Mtd2l6EAwyBQgAEIAEMgUIABCABDIFCC4QgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOg4IABCPARDqAhCMAxDlAjoLCC4QgAQQxwEQ0QM6CAguEIAEENQCUMIUWP0XYMhJaAFwAHgAgAFeiAHFApIBATSYAQCgAQGwAQg&sclient=gws-wiz")
        sleep(3)