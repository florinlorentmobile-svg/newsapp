import streamlit as st
import data_apis

def afiseaza_widgeturi():
    # Creăm 2 coloane simetrice
    col1, col2 = st.columns(2)
    
    # Preluăm datele reale din noul nostru modul
    vreme = data_apis.get_vreme()
    curs_eur, curs_usd = data_apis.get_curs_valutar()
    
    # Afișăm casetele
    with col1:
        st.metric(label="🌤️ Vremea (Buc)", value=vreme)
        
    with col2:
        # Folosim parametrul 'delta' din st.metric pentru a afișa subtil și USD-ul sub EUR
        st.metric(label="💶 EUR / RON", value=curs_eur, delta=f"USD: {curs_usd}", delta_color="off")
