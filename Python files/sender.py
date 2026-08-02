import requests

ESP_IP = "10.124.21.145"

text = "Hello from Python!"

url = f"http://{ESP_IP}/update"

try:
    response = requests.get(url,
                            params = {"text": text},
                            timeout = 3)

    print("Status:", response.status_code)
    print("Response:", response.text)

except Exception as e:
    print("Error:", e)
