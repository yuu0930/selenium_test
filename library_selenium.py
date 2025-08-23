from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import time
import os


"""chromeを開く"""
driver = webdriver.Chrome()

"""指定のページを開く"""
driver.get("https://www.library.city.hiroshima.jp/index.html")

"""ログイン画面を探す"""
login_btn = driver.find_element(By.XPATH, '//div[@id="ToolBox_My"]/p/a') # XPATHは'//親要素[@id="id名"]/子タグ'

"""ログインボタンを押す"""
login_btn.click()

"""ログインボタンを押して10秒待機"""
time.sleep(3)

""".envファイルの読み込み"""
load_dotenv()

"""環境変数を定数に代入"""
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

"""利用者ID入力欄を探してIDを入力"""
username_element = driver.find_element(By.ID, 'usercd')
username_element.send_keys(USERNAME)

"""パスワード入力欄を探してパスワードを入力"""
password_element = driver.find_element(By.ID, 'password')
password_element.send_keys(PASSWORD)

"""ログインボタンを探して押下する"""
login_btn = driver.find_element(By.NAME, 'submit_btn_login')
login_btn.click()

"""ログインボタンを押して10秒待機"""
time.sleep(10)

"""ブラウザを閉じる"""
driver.quit()