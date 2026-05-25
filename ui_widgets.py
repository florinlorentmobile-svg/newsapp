import streamlit as st
import data_apis

def afiseaza_widgeturi():
    # Preluăm datele
    vreme = data_apis.get_vreme()
    curs_eur, curs_usd = data_apis.get_curs_valutar()
    
    # CSS compactat și ajustat special pentru a nu depăși ecranul
    # S-au adăugat steagurile și formatul simetric cerut
    widget_html = f"""<div style="display: flex; gap: 10px; margin-bottom: 15px; width: 100%; box-sizing: border-box;">
    <div style="flex: 1; min-width: 0; background-color: rgba(128, 128, 128, 0.15); border-radius: 10px; padding: 12px 5px; text-align: center; border: 1px solid rgba(128, 128, 128, 0.2); display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 11px; color: #888; text-transform: uppercase; margin-bottom: 5px;">🌤️ Vremea (Buc)</div>
        <div style="font-size: 18px; font-weight: bold;">{vreme}</div>
    </div>
    <div style="flex: 1; min-width: 0; background-color: rgba(128, 128, 128, 0.15); border-radius: 10px; padding: 12px 5px; text-align: center; border: 1px solid rgba(128, 128, 128, 0.2); display: flex; flex-direction: column; justify-content: center; gap: 6px;">
        <div style="font-size: 12px; font-weight: bold; white-space: nowrap;">🇷🇴/🇪🇺 RON/EUR {curs_eur}</div>
        <div style="font-size: 12px; font-weight: bold; white-space: nowrap;">🇷🇴/🇺🇸 RON/USD {curs_usd}</div>
    </div>
</div>"""
    
    # Afișăm elementele HTML în aplicație
    st.markdown(widget_html, unsafe_allow_html=True)
