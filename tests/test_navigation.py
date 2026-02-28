import config
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigate_to_pos_direct(driver):
    wait = WebDriverWait(driver, 30)
    
    # ১. সরাসরি লগইন পেজে যাওয়া
    driver.get(config.BASE_URL)
    
    try:
        # ২. লগইন প্রসেস (সবচেয়ে সেফ XPath ব্যবহার করে)
        email_xpath = "//input[@type='email'] | //input[@name='email']"
        email_field = wait.until(EC.element_to_be_clickable((By.XPATH, email_xpath)))
        email_field.send_keys("super_user@app.dev")
        
        pass_xpath = "//input[@type='password'] | //input[@name='password']"
        password_field = driver.find_element(By.XPATH, pass_xpath)
        password_field.send_keys("test1234")
        
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()

        # ৩. ড্যাশবোর্ড লোড হওয়া পর্যন্ত অপেক্ষা করা
        wait.until(EC.url_contains("/backend/app"))
        print("\nLogin Successful!")

        # ৪. ম্যাজিক স্টেপ: সরাসরি POS ইউআরএল-এ চলে যাওয়া
        # যেহেতু মেনু ক্লিক কাজ করছে না, আমরা সরাসরি লিঙ্কে যাব
        pos_url = "https://backend-staging.caffelo.online/backend/pos"
        driver.get(pos_url)
        print(f"Navigating directly to: {pos_url}")

        # ৫. ভেরিফিকেশন: পেজটি আসলেই লোড হয়েছে কি না
        wait.until(EC.url_contains("/pos"))
        time.sleep(3) # পেজ কন্টেন্ট লোড হওয়ার সময় দিন
        
        print(f"Current URL: {driver.current_url}")
        assert "pos" in driver.current_url.lower()
        print("POS Page Loaded Successfully via Direct URL!")

    except Exception as e:
        print(f"\nDirect Navigation failed: {str(e)}")
        raise e