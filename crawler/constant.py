from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

NUMBER_OF_THREADS = 3
start_date = "18-05-2024"
end_date = "18-05-2024"

# Path to your Chrome user profile
options = webdriver.ChromeOptions()
profile_path = r"C:\Users\DELLL\AppData\Local\Google\Chrome\User Data\Default"
options.add_argument(f"user-data-dir={profile_path}")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
)
