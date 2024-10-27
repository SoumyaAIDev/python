import requests


city_name= "Bangalore"
API_key ="4052f163e5a7f80d82b9b1d2dc42f909"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"


response = requests.get(url)

if response.status_code == 200:
    print("yes ,we hit")
    data = response.json()
    print("weather is",data["weather"][0]["description"])
    print('current temperture is',data['main']['temp'])
    print('current temperture  feels like is',data['main']['feels_like'])
    print('humidity  feels like is',data['main']['humidity'])


