import config

def test_homepage_title(driver):
    driver.get(config.BASE_URL)
    
    actual_title = driver.title
    print(f"\nActual Title is: {actual_title}")
    
    # যেহেতু সাইটটি এখন লগইন পেজে রিডাইরেক্ট হচ্ছে, তাই 'Login' চেক করি
    assert "Login" in actual_title

def test_check_url(driver):
    driver.get(config.BASE_URL)
    
    # রিডাইরেক্ট হওয়ার কারণে URL-এ 'login' থাকতে পারে, তাই সেটি চেক করছি
    actual_url = driver.current_url
    print(f"Current URL is: {actual_url}")
    
    assert "login" in actual_url