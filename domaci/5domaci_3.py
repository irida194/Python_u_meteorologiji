def total_precipitation(rate, duration):
    # convert rate from mm/hour to mm/minute
    rate_per_minute = rate/60
    # convert duration from minutes to hours
    total_duration_in_hours = duration/60
    # calculate total precipitation
    total_precip = rate_per_minute * duration
    return total_precip

print(total_precipitation(10, 180))

def tp(rate,duration):
    dur_h=duration/60
    total=rate*dur_h
    return total
tp(10,180)