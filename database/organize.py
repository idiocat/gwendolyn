from numpy import isnan

def organize(data):
    for i in range(len(data)):
        target_name,mass,radius,semi_major_axis,period,eccentricity,discovered,\
            star_name,star_spec_type,star_distance,star_mass,star_radius,star_age,star_teff,star_metallicity,ra,dec =\
        data[i].get('target_name'), data[i].get('mass'), data[i].get('radius'), data[i].get('semi_major_axis'),\
            data[i].get('period'), data[i].get('eccentricity'), data[i].get('discovered'),\
                data[i].get('star_name'), data[i].get('star_spec_type'), data[i].get('star_distance'), data[i].get('star_mass'),\
                data[i].get('star_radius'), data[i].get('star_age'), data[i].get('star_teff'), data[i].get('star_metallicity'),\
                data[i].get('ra'), data[i].get('dec')

        yield f"{i + 1}. Exoplanet {target_name} (discovered at {discovered}):\n" +\
        "Mass: " + (f"{mass} Jupiter masses; " if not isnan(mass) else "unknown; ") +\
        "Radius: " + (f"{radius} Jupiter radiuses;\n" if not isnan(radius) else "unknown;\n") +\
        "Semi-major axis: " + (f"{semi_major_axis} AU; " if not isnan(semi_major_axis) else "― ; ") +\
        "Eccentricity: " + (f"{eccentricity}; " if not isnan(eccentricity) else "― ; ") +\
        "Period: " + (f"{period} days.\n" if not isnan(period) else "― ;\n") +\
        ((f"Orbiting {star_name} ({star_spec_type}) {star_distance} pc away:\n" +\
        "Mass: " + (f"{star_mass} solar masses; " if not isnan(star_mass) else "unknown; ") +\
        "Radius: " + (f"{star_radius} solar radiuses;\n" if not isnan(star_radius) else "unknown;\n") +\
        "Age: " + (f"{star_age} Gyr old; " if not isnan(star_age) else "― ; ") +\
        "Temperature: " + (f"{star_teff} K; " if not isnan(star_teff) else "― ; ") +\
        "Metallicity: " + (f"{star_metallicity};\n" if not isnan(star_metallicity) else "― ;\n"))\
            if not isnan(star_distance) else '') +\
        f"Declination: {dec}°; Right ascension: {ra}°.\n"
        