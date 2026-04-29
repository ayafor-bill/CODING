from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Define your Instagram credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Define the number of users to unfollow
UNFOLLOW_LIMIT = 5

# Initialize the Selenium WebDriver
driver = webdriver.Chrome()

def login():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    # Enter username
    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(USERNAME)

    # Enter password
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

def unfollow_users():
    # Navigate to your profile
    driver.get(f"https://www.instagram.com/{USERNAME}/")
    time.sleep(3)

    # Click on the "Following" list
    following_button = driver.find_element(By.PARTIAL_LINK_TEXT, "following")
    following_button.click()
    time.sleep(3)

    # Scroll through the list and unfollow
    for i in range(UNFOLLOW_LIMIT):
        try:
            unfollow_button = driver.find_element(By.XPATH, "//button[text()='Following']")
            unfollow_button.click()
            time.sleep(1)

            confirm_button = driver.find_element(By.XPATH, "//button[text()='Unfollow']")
            confirm_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error unfollowing user {i+1}: {e}")
            break

# Main logic
try:
    login()
    unfollow_users()
finally:
    driver.quit()