URL = "https://maps.google.com/maps?q={lat},{lon}"


def show_g(lat, lon):
    return URL.format(lat=lat, lon=lon)


Shops = [
    ("АТБ-Маркет", {
        "lat": 49.0476923,
        "lon": 38.2188943
    }),
    ("Супермаркет Семья", {
        "lat": 49.0454269,
        "lon": 38.2249238
    }),
    ("Магазин Макс", {
        "lat": 49.0375738,
        "lon": 38.2101318
    })
]
