import streamlit as st
import streamlit.components.v1 as components
import ui_sidebar
import data_news
import ui_widgets

# 1. Configurare pagină (trebuie să fie prima comandă Streamlit)
st.set_page_config(page_title="Știri Mobile", page_icon="📱", layout="centered")

# 2. Inițializare "Session State"
# Aici salvăm starea aplicației pentru a ști dacă suntem în ecranul principal sau citim o știre
if "vizualizare_articol" not in st.session_state:
    st.session_state.vizualizare_articol = None

def main():
    # 3. Afișare Meniu Lateral
    limba, tara, regiune, categorie, keyword, marime_font = ui_sidebar.genereaza_sidebar()

    # 4. Injectare CSS pentru optimizare Telefon (9:16) și limitarea textului
    st.markdown(f"""
        <style>
            /* Modificare dinamică a fontului în toată aplicația */
            html, body, [class*="st-"] {{
                font-size: {marime_font}px !important;
            }}
            /* Forțare container central să aibă lățimea unui telefon */
            .block-container {{
                max-width: 480px; 
                padding-top: 1rem;
            }}
            /* Stilizare Titlu */
            .titlu-stire {{
                font-weight: bold;
                font-size: {marime_font + 2}px;
                color: #1f77b4;
                line-height: 1.2;
                margin-bottom: 5px;
            }}
            /* Stilizare Descriere: Se trunchiază inteligent la 2 rânduri */
            .descriere-stire {{
                display: -webkit-box;
                -webkit-line-clamp: 2;
                -webkit-box-orient: vertical;  
                overflow: hidden;
                font-size: {marime_font - 1}px;
                color: #555;
                margin-bottom: 5px;
            }}
            /* Stilizare Sursă */
            .sursa-stire {{
                font-size: {marime_font - 3}px;
                color: #888;
                font-weight: bold;
                text-transform: uppercase;
                margin-bottom: 10px;
            }}
            .separator {{
                border-bottom: 1px solid #ddd;
                margin-bottom: 15px;
            }}
        </style>
    """, unsafe_allow_html=True)

    # 5. Logica de Ecrane (Rutarea)
    if st.session_state.vizualizare_articol is None:
        arata_ecran_principal(tara, regiune, categorie, keyword)
    else:
        arata_ecran_articol()

def arata_ecran_principal(tara, regiune, categorie, keyword):
    
    # 1. Afișăm widgeturile simetrice sus
    ui_widgets.afiseaza_widgeturi()
    
    # Linia de demarcație vizuală
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
    
    st.markdown("## 📰 Știri")
    
    # Apelăm funcția din data_news.py
    with st.spinner("Se caută cele mai noi articole..."):
        stiri = data_news.preia_stiri(tara, regiune, categorie, keyword)
    
    if not stiri:
        st.warning("Nu am găsit nicio știre pentru filtrele selectate sau această categorie nu există încă pentru regiunea respectivă.")
        return

    # Afișarea listei de știri cu scroll pe verticală
    for index, stire in enumerate(stiri):
        html_stire = f"""
            <div class="titlu-stire">{stire['titlu']}</div>
            <div class="descriere-stire">{stire['descriere']}</div>
            <div class="sursa-stire">Sursa: {stire['sursa']}</div>
        """
        st.markdown(html_stire, unsafe_allow_html=True)
        
        # Buton pentru deschiderea articolului complet (fără a părăsi aplicația)
        if st.button("Citește articolul", key=f"btn_{index}"):
            st.session_state.vizualizare_articol = stire['link']
            st.rerun()
            
        st.markdown('<div class="separator"></div>', unsafe_allow_html=True)

def arata_ecran_articol():
    link = st.session_state.vizualizare_articol
    
    # Butonul de Întoarcere
    if st.button("⬅️ Înapoi la Știri"):
        st.session_state.vizualizare_articol = None
        st.rerun()
        
    st.markdown('<div class="separator"></div>', unsafe_allow_html=True)
    
    # Extragem articolul cu un indicator vizual de încărcare
    with st.spinner("Se extrage articolul curat..."):
        date_articol = data_news.extrage_text_articol(link)
    
    # Dacă extragerea a reușit și avem text
    if date_articol and date_articol['text']:
        # Afișăm Titlul
        st.markdown(f"### {date_articol['titlu']}")
        
        # Afișăm Imaginea (dacă există)
        if date_articol['imagine']:
            st.image(date_articol['imagine'], use_container_width=True)
            
        # Afișăm Textul curat (folosim white-space pre-wrap pentru a păstra paragrafele)
        st.markdown(
            f"<div style='font-size: {st.session_state.get('marime_font', 15)}px; line-height: 1.6; color: #333; white-space: pre-wrap;'>{date_articol['text']}</div>", 
            unsafe_allow_html=True
        )
        
        st.markdown('<div class="separator" style="margin-top: 20px;"></div>', unsafe_allow_html=True)
        st.caption(f"[Vezi articolul original]({link})")
        
    else:
        # Plan de rezervă dacă site-ul blochează complet descărcarea (securitate maximă)
        st.error("Nu am putut extrage textul automat din cauza securității site-ului sursă.")
        st.markdown(f"[**Deschide articolul în browser aici**]({link})")

if __name__ == "__main__":
    main()
