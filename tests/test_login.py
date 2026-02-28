import config
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_admin_login(driver):
    # সাইটে যাওয়া
    driver.get(config.BASE_URL)
    
    # ১০ সেকেন্ড পর্যন্ত অপেক্ষা করবে যতক্ষণ না ইমেইল ফিল্ডটি লোড হয়
    wait = WebDriverWait(driver, 10)
    
    try:
        # ১. ইমেইল ফিল্ড খুঁজে বের করা (কয়েকটি পদ্ধতিতে চেষ্টা করবে)
        try:
            # প্রথমে 'email' নামে খুঁজার চেষ্টা
            email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        except:
            # না পেলে CSS Selector (input type email) দিয়ে খুঁজার চেষ্টা
            email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
        
        email_field.clear()
        email_field.send_keys("super_user@app.dev") # সরাসরি ইউজারনেম দিলাম নিশ্চিত হতে
        
        # ২. পাসওয়ার্ড ফিল্ড খুঁজে বের করা
        try:
            password_field = driver.find_element(By.NAME, "password")
        except:
            password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
            
        password_field.clear()
        password_field.send_keys("test1234") # সরাসরি পাসওয়ার্ড দিলাম
        
        # ৩. লগইন বাটনে ক্লিক করা
        # বাটনে ক্লিক করার আগে সেটি 'Clickable' কিনা চেক করা ভালো
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_button.click()
        
        # ৪. লগইন সফল হয়েছে কিনা তা চেক করা (URL পরিবর্তন হওয়া পর্যন্ত ৫ সেকেন্ড অপেক্ষা)
        time.sleep(5)
        current_url = driver.current_url
        print(f"\nLogin Result URL: {current_url}")
        
        # যদি URL পরিবর্তন হয় এবং তাতে 'login' না থাকে, তবে টেস্ট পাস
        assert "login" not in current_url
        print("Login Successful!")

    except Exception as e:
        print(f"Error: {str(e)}")
        raise e