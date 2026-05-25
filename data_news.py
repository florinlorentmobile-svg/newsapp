import streamlit as st
import feedparser

# Baza de date locală extinsă cu fluxuri RSS pentru România
# Structură ierarhică: Țară -> Regiune -> Categorie
RSS_FEEDS = {
    "România": {
        "Național": {
            "General": [
                {"nume": "Digi24", "url": "https://www.digi24.ro/rss"},
                {"nume": "HotNews", "url": "https://www.hotnews.ro/rss"},
                {"nume": "Adevărul", "url": "https://adevarul.ro/rss"},
                {"nume": "Știrile ProTV", "url": "https://stirileprotv.ro/rss"},
                {"nume": "G4Media", "url": "https://www.g4media.ro/feed"},
                {"nume": "Libertatea", "url": "https://www.libertatea.ro/rss"},
                {"nume": "Mediafax", "url": "https://www.mediafax.ro/rss"},
                {"nume": "B1 TV", "url": "https://www.b1tv.ro/feed"}
            ],
            "Financiar": [
                {"nume": "Ziarul Financiar", "url": "https://www.zf.ro/rss"},
                {"nume": "Economica", "url": "https://www.economica.net/feed"},
                {"nume": "Profit.ro", "url": "https://www.profit.ro/feed"},
                {"nume": "Bursa", "url": "https://www.bursa.ro/rss"},
                {"nume": "Wall-Street", "url": "https://www.wall-street.ro/rss"}
            ],
            "Sport": [
                {"nume": "Gazeta Sporturilor", "url": "https://www.gsp.ro/rss"},
                {"nume": "ProSport", "url": "https://www.prosport.ro/feed"},
                {"nume": "Sport.ro", "url": "https://www.sport.ro/rss"},
                {"nume": "Fanatik", "url": "https://www.fanatik.ro/feed"}
            ],
            "IT & Tech": [
                {"nume": "Go4IT", "url": "https://www.go4it.ro/feed/"},
                {"nume": "Mobilissimo", "url": "https://www.mobilissimo.ro/rss.xml"},
                {"nume": "ArenaIT", "url": "https://arenait.ro/feed/"},
                {"nume": "Zona IT", "url": "https://zonait.ro/feed/"}
            ],
            "Divertisment": [
                {"nume": "Cancan", "url": "https://www.cancan.ro/feed"},
                {"nume": "Click", "url": "https://click.ro/rss"},
                {"nume": "Viva", "url": "https://www.viva.ro/feed"}
            ]
        },
        "Nord": {
            "General": [
                {"nume": "Monitorul de Cluj", "url": "https://www.monitorulcj.ro/rss"},
                {"nume": "Bihoreanul", "url": "https://www.ebihoreanul.ro/rss"},
                {"nume": "Ziarul de Maramureș", "url": "https://ziaruldemaramures.ro/feed/"}
            ]
        },
        "Est": {
            "General": [
                {"nume": "Ziarul de Iași", "url": "https://www.ziaruldeiasi.ro/rss"},
                {"nume": "Monitorul de Suceava", "url": "https://www.monitorulsv.ro/rss"},
                {"nume": "Vremea Nouă (Vaslui)", "url": "https://www.vremeanoua.ro/feed/"}
            ]
        },
        "Sud": {
            "General": [
                {"nume": "Ziua de Constanța", "url": "https://www.ziuaconstanta.ro/rss.html"},
                {"nume": "Gazeta de Sud", "url": "https://www.gds.ro/feed/"},
                {"nume": "Observatorul Prahovean", "url": "https://www.observatorulph.ro/feed"}
            ]
        },
        "Vest": {
            "General": [
                {"nume": "TION (Timiș Online)", "url": "https://www.tion.ro/feed/"},
                {"nume": "Aradon", "url": "https://www.aradon.ro/feed/"},
                {"nume": "Express de Banat", "url": "https://expressdebanat.ro/feed/"}
            ]
        }
    }
}

@st.cache_data(ttl=600)

def preia_stiri(tara, regiune, categorie, keyword=""):
    """
    Se conectează la sursele RSS pe baza filtrelor și returnează o listă de știri.
    A fost adăugat parametrul 'regiune' pentru a respecta logica aplicației.
    """
    stiri_gasite = []
    
    # Navigăm în siguranță prin dicționar pentru a evita erorile dacă o categorie lipsește
    if tara in RSS_FEEDS and regiune in RSS_FEEDS[tara] and categorie in RSS_FEEDS[tara][regiune]:
        surse = RSS_FEEDS[tara][regiune][categorie]
        
        for sursa in surse:
            # feedparser extrage datele de la URL
            feed = feedparser.parse(sursa["url"])
            
            # Limităm la primele 15-20 articole pe sursă pentru a asigura încărcarea rapidă pe telefon
            for articol in feed.entries[:20]:
                titlu = articol.get("title", "")
                descriere = articol.get("description", "")
                link = articol.get("link", "")
                
                # Filtrare după cuvânt cheie
                if keyword:
                    if keyword.lower() not in titlu.lower() and keyword.lower() not in descriere.lower():
                        continue 
                
                stiri_gasite.append({
                    "titlu": titlu,
                    "descriere": descriere,
                    "link": link,
                    "sursa": sursa["nume"]
                })
                
    return stiri_gasite

from newspaper import Article

def extrage_text_articol(url):
    """
    Descarcă pagina web și extrage doar textul util și imaginea principală,
    fără reclame, cookie-uri sau meniuri.
    """
    try:
        # Inițializăm articolul
        articol = Article(url)
        # Descărcăm conținutul
        articol.download()
        # Îl parsăm (extragem informațiile structurate)
        articol.parse()
        
        return {
            "titlu": articol.title,
            "imagine": articol.top_image,
            "text": articol.text
        }
    except Exception as e:
        print(f"Eroare la extragerea articolului: {e}")
        return None
