import requests
import streamlit as st

@st.cache_data(ttl=1800) # Memorăm vremea pentru 30 de minute (1800 secunde)
def get_vreme(lat=44.4323, lon=26.1063):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status() 
        data = response.json()
        temp = data['current_weather']['temperature']
        return f"{temp} °C"
    except Exception as e:
        print(f"Eroare preluare meteo: {e}")
        return "-- °C"

@st.cache_data(ttl=3600) # Memorăm cursul valutar pentru 1 oră (3600 secunde)
def get_curs_valutar():
    try:
        url_eur = "https://open.er-api.com/v6/latest/EUR"
        resp_eur = requests.get(url_eur, timeout=5).json()
        eur_ron = resp_eur['rates']['RON']
        
        url_usd = "https://open.er-api.com/v6/latest/USD"
        resp_usd = requests.get(url_usd, timeout=5).json()
        usd_ron = resp_usd['rates']['RON']
        
        return f"{eur_ron:.2f}", f"{usd_ron:.2f}"
    except Exception as e:
        print(f"Eroare preluare valută: {e}")
        return "--", "--"
