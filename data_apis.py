import requests

def get_vreme(lat=44.4323, lon=26.1063):
    try:
        # Adăugăm un User-Agent pentru a preveni blocarea cererii de către server
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        # Am crescut timeout-ul la 5 secunde
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status() # Forțăm ridicarea unei erori dacă HTTP-ul pică
        
        data = response.json()
        temp = data['current_weather']['temperature']
        return f"{temp} °C"
    except Exception as e:
        # Dacă pică, eroare va apărea în terminalul editorului tău pentru a o putea repara
        print(f"Eroare preluare meteo: {e}")
        return "-- °C"

def get_curs_valutar():
    try:
        url_eur = "https://open.er-api.com/v6/latest/EUR"
        resp_eur = requests.get(url_eur, timeout=5).json()
        eur_ron = resp_eur['rates']['RON']
        
        url_usd = "https://open.er-api.com/v6/latest/USD"
        resp_usd = requests.get(url_usd, timeout=5).json()
        usd_ron = resp_usd['rates']['RON']
        
        # Eliminăm cuvântul "Lei" pentru că face textul prea lung în casetă. Păstrăm doar numărul.
        return f"{eur_ron:.2f}", f"{usd_ron:.2f}"
    except Exception as e:
        print(f"Eroare preluare valută: {e}")
        return "--", "--"
