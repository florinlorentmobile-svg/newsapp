import streamlit as st
import data_apis

def afiseaza_widgeturi():
    # Preluăm datele
    vreme = data_apis.get_vreme()
    curs_eur, curs_usd = data_apis.get_curs_valutar()
    
    # Am adăugat margin-top: 35px pentru a nu se mai tăia sus.
    # Am înlocuit emoji-urile (care nu merg pe Windows) cu imagini reale ale steagurilor (16px).
    widget_html = f"""<div style="display: flex; gap: 10px; margin-top: 35px; margin-bottom: 20px; box-sizing: border-box;">
    <div style="flex: 1; background-color: rgba(128, 128, 128, 0.15); border-radius: 10px; padding: 15px 5px; text-align: center; border: 1px solid rgba(128, 128, 128, 0.2); box-sizing: border-box; display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 11px; color: #888; text-transform: uppercase; margin-bottom: 5px;">🌤️ Vremea (Buc)</div>
        <div style="font-size: 19px; font-weight: bold;">{vreme}</div>
    </div>
    <div style="flex: 1; background-color: rgba(128, 128, 128, 0.15); border-radius: 10px; padding: 10px 5px; text-align: center; border: 1px solid rgba(128, 128, 128, 0.2); box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; gap: 8px;">
        <div style="display: flex; align-items: center; justify-content: center; gap: 6px; font-size: 13px; font-weight: bold;">
            <img src="https://flagcdn.com/w20/ro.png" width="16" style="border-radius: 2px;"> / <img src="https://flagcdn.com/w20/eu.png" width="16" style="border-radius: 2px;"> {curs_eur}
        </div>
        <div style="display: flex; align-items: center; justify-content: center; gap: 6px; font-size: 13px; font-weight: bold;">
            <img src="https://flagcdn.com/w20/ro.png" width="16" style="border-radius: 2px;"> / <img src="https://flagcdn.com/w20/us.png" width="16" style="border-radius: 2px;"> {curs_usd}
        </div>
    </div>
</div>"""
    
    # Afișăm elementele HTML în aplicație
    st.markdown(widget_html, unsafe_allow_html=True)
