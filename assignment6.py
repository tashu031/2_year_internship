import requests

def weather_data(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ddf7424369f83dd8a744e254f0f88c66&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        print("\n------ Weather Report ------")

        print("City :", data['name'])
        print("Country :", data['sys']['country'])

        print("Temperature :", data['main']['temp'], "°C")
        print("Feels Like :", data['main']['feels_like'], "°C")

        print("Minimum Temp :", data['main']['temp_min'], "°C")
        print("Maximum Temp :", data['main']['temp_max'], "°C")

        print("Humidity :", data['main']['humidity'], "%")
        print("Pressure :", data['main']['pressure'], "hPa")

        print("Weather :", data['weather'][0]['main'])
        print("Description :", data['weather'][0]['description'])

        print("Wind Speed :", data['wind']['speed'], "m/s")

    except requests.exceptions.RequestException as e:
        print("Error :", e)

city = input("Enter the city : ")
weather_data(city)
















# ................................ROCK _ PAPER _SCISSOR GAME   ........................ ............
import random

l =["rock" ,'paper' ,'scissor']

ch = int(input("enter your choice (1 = YES ,I Am ready ) , 2 = No : "))
if ch == 1:
    uscore =0
    cscore =0
    for i in range(1,6):
        uch = input("enter your choice (rock ,  paper , scissor)  :")
        cch = random.choice(l)

        if(uch == cch ):
            uscore+=1
            cscore+=1
            print("Game Draw ")
        elif((uch == "rock" and cch == "scissor")or (uch == "paper" and cch == "rock") or (uch == "scissor" and cch =="paper")):
            uscore +=1
            print("you won")
        elif((cch == "rock" and uch == "scissor") or (cch == "paper" and uch == "rock") or (cch == "scissor" and uch == "paper")):
            cscore+=1
            print("computer win")
        else:
            print("Please Enter right choice !")

    print("\nFinal result :")
    print(f"Your score :{uscore} \nComputer score : {cscore}")
    if(uscore == cscore):
        print("Match Draw")
    elif(uscore> cscore):
        print("You win")
    else:
        print("you lose")

elif ch==2 :
    print("Next Time")


    

import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

data = response.json()

print("Setup :", data['setup'])
print("Punchline :", data['punchline'])
