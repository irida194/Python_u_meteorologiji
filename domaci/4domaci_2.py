# Vertical temperature profile of the atmosphere
atmosphere_profile = {
    'troposphere': {
        'altitude': 0,     # in kilometers
        'temperature': 15  # in Celsius
    },
    'stratosphere': {
        'altitude': 10,
        'temperature': -50
    },
    'mesosphere': {
        'altitude': 50,
        'temperature': -70
    },
    'thermosphere': {
        'altitude': 100,
        'temperature': 150
    }
}

def temperature_at_altitude(altitude):
    # Function to get the temperature at a given altitude in the atmosphere
    layers = list(atmosphere_profile.keys())
    for i in range(len(layers) - 1):
        layer1 = atmosphere_profile[layers[i]]
        layer2 = atmosphere_profile[layers[i + 1]]
        if layer1['altitude'] <= altitude < layer2['altitude']:
            temp1 = layer1['temperature']
            temp2 = layer2['temperature']
            alt1 = layer1['altitude']
            alt2 = layer2['altitude']
            lapse_rate = (temp2 - temp1) / (alt2 - alt1)
            return temp1 + lapse_rate * (altitude - alt1)

    # If the altitude is above the highest layer, return the temperature of the highest layer
    highest_layer = atmosphere_profile[layers[-1]]
    return highest_layer['temperature']

# Example usage:
altitude = float(input("Enter altitude (in kilometers): "))
temperature = temperature_at_altitude(altitude)
print(f"The temperature at {altitude} kilometers is {temperature}°C.")