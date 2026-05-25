import streamlit as st
import data_apis

def afiseaza_widgeturi():
    # Preluăm datele
    vreme = data_apis.get_vreme()
    curs_eur, curs_usd = data_apis.get_curs_valutar()
    
    # Construim casetele direct cu HTML/CSS pentru un aspect nativ de mobil
    # Folosim culori semi-transparente (rgba) pentru a arăta bine și pe modul de noapte și pe modul de zi
    widget_html = f"""
    <div style="display: flex; gap: 15px; margin-bottom: 20px;">
        <div style="flex: 1; background-color: rgba(128, 128, 128, 0.15); border-radius: 15px; padding: 15px; text-align: center; border: 1px solid rgba(128, 128, 128, 0.2);">
            <div style="font-size: 13px; color: #888; text-transform: uppercase; margin-bottom: 5px;">🌤️ Vremea (Buc)</div>
            <div style="font-size: 20px; font-weight: bold;">{vreme}</div>
        </div>
        
        <div style="flex: 1; background-color: rgba(128, 128, 128, 0.15); border-radius: 15px; padding: 15px; text-align: center; border: 1px solid rgba(128, 128, 128, 0.2);">
            <div style="font-size: 13px; color: #888; text-transform: uppercase; margin-bottom: 5px;">💶 EUR/RON</div>
            <div style="font-size: 20px; font-weight: bold;">{curs_eur}</div>
            <div style="font-size: 12px; color: #888; margin-top: 5px;">USD: {curs_usd}</div>
        </div>
    </div>
    """
    
    # Afișăm elementele HTML în aplicație
    st.markdown(widget_html, unsafe_allow_html=True)
