import re

# Example METAR report
metar_report = "METAR LYBE 160600Z 26007KT 230V290 CAVOK 07/06 Q1021 NOSIG="

pressure_pattern = re.compile(r'Q(\d{4})')

pressure_match = pressure_pattern.search(metar_report)

if pressure_match:
    pressure = int(pressure_match.group(1))
    print(f"Pritisak je (QNH): {pressure} hPa")
else:
    print("Pritisak nije pronadjen")
    

import re

metar_report = "METAR LYBE 160600Z 26007KT 230V290 CAVOK 07/06 Q1021 NOSIG="

wind_pattern = re.compile(r'(\d{3})KT')

wind_match = wind_pattern.search(metar_report)

if wind_match:
    wind= int(wind_match.group(1))
    print(f"Wind: {wind} kt")
else:
    print("Nije pronadjen vetar")
    
import re

metar_reports = [
    "METAR LYBE 160600Z 26007KT 230V290 CAVOK 07/06 Q1021 NOSIG=",
    "METAR LYBT 160630Z 26006KT CAVOK 07/07 Q1022 NOSIG=",
    "METAR LYKV 160630Z 00000KT CAVOK 02/02 Q1023 NOSIG=",
    "METAR LYNI 160600Z 00000KT 7000 SCT050 07/07 Q1022 NOSIG="
]

pressure_pattern = re.compile(r'Q(\d{4})')

for metar_report in metar_reports:
    pressure_match = pressure_pattern.search(metar_report)

    if pressure_match:
        pressure = int(pressure_match.group(1))
        print(f"Atmospheric Pressure (QNH): {pressure} hPa")
    else:
        print(f"nema pritiska")