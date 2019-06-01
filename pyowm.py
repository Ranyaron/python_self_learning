import pyowm

owm = pyowm.OWM('8861ead3-676d-4304-8f23-5cdd7f3c4cc7')
observation = owm.weather_at_place('Москва')
w = observation.get_weather()
print(w)