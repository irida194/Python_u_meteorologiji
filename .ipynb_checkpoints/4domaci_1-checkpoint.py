def calculate_average_temperature(weather_data):
    # Calculate the average temperature for the month
    total_temperature = sum(weather_data['temperature'])
    num_days = len(weather_data['temperature'])
    return total_temperature / num_days

def calculate_total_precipitation(weather_data):
    # Calculate the total precipitation for the month
    return sum(weather_data['precipitation'])

def find_hottest_day(weather_data):
    # Find the day with the highest temperature
    max_temp = max(weather_data['temperature'])
    hottest_day = weather_data['temperature'].index(max_temp) + 1
    return hottest_day

def find_rainy_days(weather_data):
    # Find the days with precipitation above a threshold (e.g., 5 mm)
    no=0
    rainy_days=[]
    for prec in weather_data['precipitation']:
        no=no+1
        if prec > 5:
            rainy_days.append(no)
    return rainy_days

# Example weather data for a month (temperature in Celsius and precipitation in mm)
weather_data = {
    'temperature': [28, 30, 32, 29, 27, 26, 24, 25, 26, 28, 30, 31, 29, 30, 31, 32, 33, 31, 30, 28, 27, 26, 28, 29, 30, 31, 32, 33, 34, 32],
    'precipitation': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 10, 7, 6, 0, 0, 0, 0, 0, 0, 0]
}

average_temperature = calculate_average_temperature(weather_data)
total_precipitation = calculate_total_precipitation(weather_data)
hottest_day = find_hottest_day(weather_data)
rainy_days = find_rainy_days(weather_data)

print("Weather data for the month:")
print("Average Temperature:", average_temperature, "°C")
print("Total Precipitation:", total_precipitation, "mm")
print("Hottest Day:", hottest_day)
print("Rainy Days:", rainy_days)