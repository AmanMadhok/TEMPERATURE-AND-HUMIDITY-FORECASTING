import pyowm
from timezone_conversion import gmt_to_eastern

API_KEY = '2b62511b3bb14c8fbb75f8103ccb9f73'

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()

def get_humidity(City):
    days = []
    dates = []
    humidity = []

    forecaster = mgr.forecast_at_place(City, '3h')
    forecast = forecaster.forecast

    for weather in forecast:
        day = gmt_to_eastern(weather.reference_time())
        date = day.date()
        if date not in dates:
            if len(days)>=3:
                return(days, humidity)
            dates.append(date)
            humidity.append(weather.humidity)
            days.append(date)
        if day.hour in[11,12,13]:
            humidity[-1] = weather.humidity

if __name__ == '__main__':
    get_humidity(City)
