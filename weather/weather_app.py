# Import project Libraries
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


# API's url
city_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

# Config file gets the key for the API
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']

# Function to get the data showed on the app
def get_weather(city):
    result = requests.get(city_url.format(city, api_key))
    if result:
        json = result.json()
        # json data Format - City, Country, temp_celsius, temp_fahrenheit, icon, wheather.
        # use https://jsonformatter.curiousconcept.com/ to organize the json API's output.
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32 
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather)
        return final

    else:
        return None

# Function to the app's search engine
def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        img['file'] = 'icons/{}.png'.format(weather[4])
        temp_lbl['text'] = '{:.1f}°C - {:.1f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]
    else:
        messagebox.showerror("Error", "Can't find city {}".format(city))

# Definitions of the app's elements, configs.
app = Tk()
app.title('Weather App')
app.geometry('300x400')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search City', width=12, command=search)
search_btn.pack()

location_lbl = Label(app, text='', font=('bold', 20))
location_lbl.pack()

img = PhotoImage(file='')
Image = Label(app, image=img)
Image.pack()

image = Label(app, bitmap='')
image.pack()

temp_lbl = Label(app, text='', font=('bold', 15))
temp_lbl.pack()

weather_lbl = Label(app, text='', font=('bold', 18))
weather_lbl.pack()


app.mainloop()