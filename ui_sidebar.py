import streamlit as st

def genereaza_sidebar():
    st.sidebar.header("⚙️ Setări și Filtre")
    
    # 1. Limba
    limba = st.sidebar.selectbox("Limbă", ["RO", "EN", "DE"])
    
    # 2. Țara (Ajustăm dinamic în funcție de limbă, dar setăm România ca implicit)
    tari_disponibile = ["România", "Germania"] if limba in ["RO", "DE"] else ["România"]
    tara = st.sidebar.selectbox("Țară", tari_disponibile)
    
    # 3. Regiunea
    regiuni = ["Național", "Nord", "Sud", "Est", "Vest"]
    regiune = st.sidebar.selectbox("Regiune", regiuni)
    
    # 4. Categoria
    categorii = ["General", "Financiar", "Sport", "IT & Tech", "Divertisment"]
    categorie = st.sidebar.selectbox("Categorie", categorii)
    
    # 5. Căutare Keyword
    keyword = st.sidebar.text_input("🔍 Căutare cuvânt cheie", placeholder="ex. Romania")
    
    # 6. Mărime font (optim pentru a citi ușor pe telefon)
    marime_font = st.sidebar.slider("Mărime Font (px)", min_value=12, max_value=24, value=15)
    
    return limba, tara, regiune, categorie, keyword, marime_font
