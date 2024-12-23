import sqlite3

# Kart bilgilerini getiren fonksiyon
def get_card_data(card_name):
    conn = sqlite3.connect('tarot.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cards WHERE name=?', (card_name,))
    card = c.fetchone()
    conn.close()
    return card

# Kartların anlamlarını ve kullanıcıdan alınan niyeti birleştirerek yorumlama yapan fonksiyon
def interpret_cards(spread, keywords):
    interpretations = []
    for card, position in spread:
        card_data = get_card_data(card)  # Veritabanından kart verilerini alın
        if position == "dikey":
            meaning = card_data[1]  # Dikey anlam
        else:
            meaning = card_data[2]  # Ters anlam
        
        # Bağlama göre yorum ekleyin
        if "aşk" in keywords:
            context = "aşk"
        elif "iş" in keywords:
            context = "iş"
        else:
            context = "genel"
        
        interpretations.append(f"Kart: {card}, Anlam: {meaning}, Bağlam: {context}")
    return interpretations

# Örnek kullanım
if __name__ == "__main__":
    # Örnek yayılım ve anahtar kelimeler
    spread = [("Aşıklar", "dikey"), ("Ölüm", "ters"), ("Güneş", "dikey")]
    keywords = ["aşk"]
    interpretations = interpret_cards(spread, keywords)
    for interp in interpretations:
        print(interp)