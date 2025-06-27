import smtplib
import time
import requests
import datetime

MY_EMAIL = "josephpaulrebert1999@gmail.com"
MY_PASSWORD = "paul5477"
MY_LAT = 30.123949
MY_LNG = -91.829048
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


def check_iss_pos():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_lat >= MY_LAT + 5 and MY_LNG - 5 <= iss_lng >= MY_LNG + 5:
        return True
    return False

def is_night():
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

while True:
    print("CHECKING")
    time.sleep(60)
    if check_iss_pos() and is_night():
        print("SENT")
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: IT WORKS!!"
        )