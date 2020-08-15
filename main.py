import eel, pyowm

eel.init('web')
eel.start('main.html', size = (700, 700))

owm = pyowm.OWM("82d316a00d15abac99bcece89526656b")
@eel.expose
def get_weather(place:str) -> str:
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    return str(temp)