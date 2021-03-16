import requests
from datetime import *
from tkinter import *
from tkinter import messagebox as mb

window = Tk()
window.title("Weather Application")
window.geometry("800x400")
window.resizable(0, 0)

#Class which contains program
class weatherApp:
    def __init__(self):
        self.city = Entry(window)
        CityLabel = Label(window, text='Please enter city name:', bg='green')
        findBtn = Button(window, text="Find", command=self.cityWeather)
        self.NameLabel = Label(window, bg='yellow')
        self.TempLabel = Label(window, bg='blue')
        self.HumidLabel = Label(window, bg='red')
        self.WindLabel = Label(window, bg='orange')
        self.CloudLabel = Label(window, bg='grey')

        #Positions
        CityLabel.place(x=140,y=5)
        self.city.place(x=300,y=5)
        findBtn.place(x=280,y=50)
        self.NameLabel.place(x=170,y=90)
        self.TempLabel.place(x=50,y=130)
        self.HumidLabel.place(x=50,y=170)
        self.WindLabel.place(x=50, y=210)
        self.CloudLabel.place(x=50,y=250)

    #Algorith
    def cityWeather(self):
        #using a try-except to catch exceptiond
        try:
            #get information from weather API
            #if successful it continues and accesses the json info and tries to fetch some data
            url = 'https://api.openweathermap.org/data/2.5/weather?q='+self.city.get()+'&appid=ab880098671bf03762a6496f504b024c'
            req = requests.get(url)
            req_j = req.json()
            temp = req_j['main']['temp']
            temp = round(float(temp)-273, 2)
        except Exception as e:
            mb.showerror('FATAL!','Can\'t find the object.\nPlease enter valid input and ensure your connection')

        #collect specific data from API

        humid = req_j['main']['humidity']

        wind = req_j['wind']['speed']

        cloud = req_j['weather'][0]['description']

        #timezone adjustments
        time = int(req_j['timezone']/3600)
        delta = time-2
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        new_time = now + timedelta(hours=delta)
        new_time = new_time.strftime("%H:%M")

        #updating labels
        self.NameLabel['font'] = 'bold',15
        self.NameLabel['text'] = 'Current '+self.city.get()+' weather, as at '+new_time+':'
        self.TempLabel['text'] = '>> Temperature: '+str(temp)+'°C'
        self.HumidLabel['text'] = '>> Humidity: '+str(humid)
        self.WindLabel['text'] = '>> Wind speed: '+str(wind)+' kmh'
        self.CloudLabel['text'] = '>> Cloud cover: '+str(cloud)


run = weatherApp()
window.mainloop()
