import pyvo

service = pyvo.dal.TAPService("http://voparis-tap-planeto.obspm.fr/tap")
params = "target_name,mass,radius,semi_major_axis,period,eccentricity,discovered,star_name,star_spec_type,star_distance,star_mass,star_radius,star_age,star_teff,star_metallicity,ra,dec"

def do_job(query: str):
    job = service.submit_job(query)
    job = service.submit_job(query)
    job.run()
    while job.phase == 'EXECUTING':
        pass
    results = job.fetch_result()
    job.delete()
    return results

def go_high(prop: str, amount: int):
    query = f"SELECT TOP {amount} {params} FROM (SELECT * FROM exoplanet.epn_core WHERE {prop} IS NOT NULL ORDER BY {prop} DESC) AS whateves"
    return do_job(query)

def go_low(prop: str, amount: int):
    query = f"SELECT TOP {amount} {params} FROM (SELECT * FROM exoplanet.epn_core WHERE {prop} IS NOT NULL ORDER BY {prop} ASC) AS whateves"
    return do_job(query)

def go_custom(prop: str, range: str, order: str, amount: int):
    value_min, value_max = range.split('-')
    query = f"SELECT TOP {amount} {params} FROM (SELECT * FROM exoplanet.epn_core WHERE ({prop} > {value_min} AND {prop} < {value_max}) ORDER BY {prop} {order}) AS whateves"
    return do_job(query)
