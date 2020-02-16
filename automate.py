import requests
import base64
from selenium import webdriver

def invitation_code():
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    }
    request = session.post("https://www.hackthebox.eu/api/invite/generate",headers=headers)
    text = request.text
    code = text.split("\"")[7]
    decoded_code = base64.b64decode(code).decode('ascii')
    return decoded_code

def automate_invitation():
    browser = webdriver.Chrome()
    browser.get("https://www.hackthebox.eu/invite")
    box = browser.find_element_by_id("code")
    box.send_keys(invitation_code())
    box.submit()

automate_invitation()

