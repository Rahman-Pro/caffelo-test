import requests
import config

def test_api_status():
    # সরাসরি সার্ভারে রিকোয়েস্ট পাঠানো
    response = requests.get(config.BASE_URL)
    print(f"\nAPI Response Code: {response.status_code}")
    
    # স্ট্যাটাস কোড ২০০ (Success) কিনা চেক করা
    assert response.status_code == 200