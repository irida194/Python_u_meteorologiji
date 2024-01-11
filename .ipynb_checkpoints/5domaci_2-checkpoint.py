import math

def relative_humidity(dew_point, temperature):
    # Calculation of saturation vapor pressure using Teten's formula
    a = 17.27
    b = 237.7
    alpha = ((a * dew_point) / (b + dew_point)) + math.log(dew_point/100)
    # Calculation of actual vapor pressure
    beta = ((a * temperature) / (b + temperature)) + math.log(temperature/100)
    # Calculation of relative humidity
    rh = 100 * math.exp(alpha - beta)
    return rh

print(relative_humidity(20, 25))