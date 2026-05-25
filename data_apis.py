import requests

def get_vreme(lat=44.4323, lon=26.1063):
    """
    Preluăm vremea de la Open-Meteo. 
    Implicit, coordonatele sunt pentru București.
    În Streamlit este dificil să preiei GPS-ul exact al telefonului din motive de securitate a browserului, 
    așa că folosim un oraș fix pentru acest prototip.
    """
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url, timeout=3).json()
        temp = response['current_weather']['temperature']
        return f"{temp} °C"
    except:
        return "-- °C"

def get_curs_valutar():
    """
    Preluăm cursul valutar RON/EUR și RON/USD folosind un API gratuit.
    """
    try:
        # Curs EUR
        url_eur = "https://open.er-api.com/v6/latest/EUR"
        resp_eur = requests.get(url_eur, timeout=3).json()
        eur_ron = resp_eur['rates']['RON']
        
        # Curs USD
        url_usd = "https://open.er-api.com/v6/latest/USD"
        resp_usd = requests.get(url_usd, timeout=3).json()
        usd_ron = resp_usd['rates']['RON']
        
        return f"{eur_ron:.2f} Lei", f"{usd_ron:.2f} Lei"
    except:
        return "-- Lei", "-- Lei"
