import eel, pyowm

owm = pyowm.OWM("")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    return "In " + str(place) + " " + str(temp) + " celsius now"


eel.init('web')
eel.start('main.html')
