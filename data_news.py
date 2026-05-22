import feedparser

# Baza de date locală cu fluxuri RSS pentru România
# Putem adăuga ulterior sute de link-uri aici
RSS_FEEDS = {
    "România": {
        "General": [
            {"nume": "Digi24", "url": "https://www.digi24.ro/rss"},
            {"nume": "HotNews", "url": "https://www.hotnews.ro/rss"}
        ],
        "Financiar": [
            {"nume": "Ziarul Financiar", "url": "https://www.zf.ro/rss"}
        ],
        "Sport": [
            {"nume": "Gazeta Sporturilor", "url": "https://www.gsp.ro/rss"}
        ],
        "Divertisment": [
            {"nume": "Libertatea", "url": "https://www.libertatea.ro/rss"}
        ]
    }
}

def preia_stiri(tara, categorie, keyword=""):
    """
    Se conectează la sursele RSS pe baza filtrelor și returnează o listă de știri.
    """
    stiri_gasite = []
    
    # Verificăm dacă există țara și categoria în baza noastră de date
    if tara in RSS_FEEDS and categorie in RSS_FEEDS[tara]:
        surse = RSS_FEEDS[tara][categorie]
        
        for sursa in surse:
            # feedparser extrage datele de la URL-ul publicației
            feed = feedparser.parse(sursa["url"])
            
            for articol in feed.entries:
                titlu = articol.get("title", "")
                descriere = articol.get("description", "")
                link = articol.get("link", "")
                
                # Dacă avem un cuvânt cheie, filtrăm știrile care nu îl conțin în titlu sau descriere
                if keyword:
                    if keyword.lower() not in titlu.lower() and keyword.lower() not in descriere.lower():
                        continue # Sărim peste această știre dacă nu conține cuvântul cheie
                
                # Adăugăm știrea în format structurat în lista noastră
                stiri_gasite.append({
                    "titlu": titlu,
                    "descriere": descriere,
                    "link": link,
                    "sursa": sursa["nume"]
                })
                
    return stiri_gasite
