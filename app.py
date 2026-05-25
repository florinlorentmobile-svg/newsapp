import streamlit as st
import streamlit.components.v1 as components
import ui_sidebar
import data_news
import ui_widgets

# 1. Configurare pagină (trebuie să fie prima comandă Streamlit)
st.set_page_config(page_title="Știri Mobile", page_icon="📱", layout="centered")

# 2. Inițializare "Session State"
if "vizualizare_articol" not in st.session_state:
    st.session_state.vizualizare_articol = None

def main():
    # 3. Afișare Meniu Lateral
    limba, tara, regiune, categorie, keyword, marime_font = ui_sidebar.genereaza_sidebar()

    # 4. Injectare CSS pentru optimizare Telefon (9:16) și limitarea textului în liste
    st.markdown(f"""
        <style>
            html, body, [class*="st-"] {{
                font-size: {marime_font}px !important;
            }}
            .block-container {{
                max-width: 480px; 
                padding-top: 1rem;
            }}
            .titlu-stire {{
                font-weight: bold;
                font-size: {marime_font + 2}px;
                color: #1f77b4;
                line-height: 1.2;
                margin-bottom: 5px;
            }}
            .descriere-stire {{
                display: -webkit-box;
                -webkit-line-clamp: 2;
                -webkit-box-orient: vertical;  
                overflow: hidden;
                font-size: {marime_font - 1}px;
                color: #555;
                margin-bottom: 5px;
            }}
            .sursa-stire {{
                font-size: {marime_font - 3}px;
                color: #888;
                font-weight: bold;
                text-transform: uppercase;
                margin-bottom: 10px;
            }}
            .separator {{
                border-bottom: 1px solid rgba(128, 128, 128, 0.2);
                margin-bottom: 15px;
            }}
        </style>
    """, unsafe_allow_html=True)

    # 5. Logica de Ecrane (Rutarea) - Pasăm mărimea fontului mai departe
    if st.session_state.vizualizare_articol is None:
        arata_ecran_principal(tara, regiune, categorie, keyword)
    else:
        arata_ecran_articol(marime_font)

def arata_ecran_principal(tara, regiune, categorie, keyword):
    ui_widgets.afiseaza_widgeturi()
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
    st.markdown("## 📰 Știri")
    
    with st.spinner("Se caută cele mai noi articole..."):
        stiri = data_news.preia_stiri(tara, regiune, categorie, keyword)
    
    if not stiri:
        st.warning("Nu am găsit nicio știre pentru filtrele selectate.")
        return

    for index, stire in enumerate(stiri):
        html_stire = f"""
            <div class="titlu-stire">{stire['titlu']}</div>
            <div class="descriere-stire">{stire['descriere']}</div>
            <div class="sursa-stire">Sursa: {stire['sursa']}</div>
        """
        st.markdown(html_stire, unsafe_allow_html=True)
        
        if st.button("Citește articolul", key=f"btn_{index}"):
            st.session_state.vizualizare_articol = stire['link']
            st.rerun()
            
        st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

def arata_ecran_articol(marime_font):
    link = st.session_state.vizualizare_articol
    
    # CSS local aplicat doar pe acest ecran pentru a face butonul mic și plat (flat)
    st.markdown("""
        <style>
            div.stButton > button {
                padding: 2px 10px !important;
                font-size: 12px !important;
                min-height: auto !important;
                height: 28px !important;
                width: auto !important;
                background-color: transparent !important;
                color: inherit !important;
                border: 1px solid rgba(128, 128, 128, 0.4) !important;
                border-radius: 5px !important;
                font-weight: 500 !important;
                box-shadow: none !important;
                transition: all 0.2s ease;
            }
            div.stButton > button:hover {
                background-color: rgba(128, 128, 128, 0.1) !important;
                border-color: rgba(128, 128, 128, 0.6) !important;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Butonul de Întoarcere optimizat (mic și plat)
    if st.button("⬅️ Înapoi"):
        st.session_state.vizualizare_articol = None
        st.rerun()
        
    st.markdown('<div class="separator" style="margin-top: 5px; margin-bottom: 15px;"></div>', unsafe_allow_html=True)
    
    with st.spinner("Se extrage articolul curat..."):
        date_articol = data_news.extrage_text_articol(link)
    
    if date_articol and date_articol['text']:
        st.markdown(f"### {date_articol['titlu']}")
        
        if date_articol['imagine']:
            st.image(date_articol['imagine'], use_container_width=True)
            
        # Stil font optimizat: adaptiv la fundal (color: inherit) și font curat de cititor digital
        st.markdown(
            f"""<div style="
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                font-size: {marime_font}px; 
                line-height: 1.6; 
                color: inherit; 
                white-space: pre-wrap;
                font-weight: 400;
                letter-spacing: -0.01em;
            ">{date_articol['text']}</div>""", 
            unsafe_allow_html=True
        )
        
        st.markdown('<div class="separator" style="margin-top: 20px;"></div>', unsafe_allow_html=True)
        st.caption(f"[Vezi articolul original]({link})")
        
    else:
        st.error("Nu am putut extrage textul automat din cauza securității site-ului sursă.")
        st.markdown(f"[**Deschide articolul în browser aici**]({link})")

if __name__ == "__main__":
    main()
