import random

# Kart listesini oluşturun (JSON'dan veya veritabanından yükleyebilirsiniz)
deck = [
    "Deli", "Büyücü","Başrahibe","İmparatoriçe","İmparator","Aziz","Aşıklar","Savaş Arabası","Güç","Ermiş","Kader Çarkı","Adalet","Asılan Adam","Ölüm","Denge","Şeytan","Kule","Yıldız",
"Ay","Güneş","Mahkeme","Dünya","As Kupa","İkili Kupa","Üçlü Kupa","Dörtlü Kupa","Beşli Kupa","Altılı Kupa","Yedili Kupa","Sekizli Kupa","Dokuzlu Kupa","Onlu Kupa","Vale Kupa",
"Şövalye Kupa","Kraliçe Kupa","Kral Kupa","As Kılıç","İkili Kılıç","Üçlü Kılıç","Dörtlü Kılıç","Beşli Kılıç","Altılı Kılıç","Yedili Kılıç","Sekizli Kılıç","Dokuzlu Kılıç","Onlu Kılıç",
"Vale Kılıç","Şövalye Kılıç","Kraliçe Kılıç","Kral Kılıç","As Değnek","İkili Değnek","Üçlü Değnek","Dörtlü Değnek","Beşli Değnek","Altılı Değnek","Yedili Değnek","Sekizli Değnek",
"Dokuzlu Değnek","Onlu Değnek","Vale Değnek","Şövalye Değnek","Kraliçe Değnek","Kral Değnek","As Para","İkili Para","Üçlü Para","Dörtlü Para","Beşli Para","Altılı Para","Yedili Para",
"Sekizli Para","Dokuzlu Para","Onlu Para","Vale Para","Şövalye Para","Kraliçe Para","Kral Para"
]

# Rastgele bir kart çeken ve desteden çıkaran fonksiyon
def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)  # Çekilen kartı desteden çıkarın
    return card

# Rastgele olarak kartın dikey veya ters pozisyonda olduğunu belirleyen fonksiyon
def card_position():
    return random.choice(["dikey", "ters"])

# 3 kartlık yayılım fonksiyonu (geçmiş, şimdi, gelecek)
def three_card_spread(deck):
    spread = [draw_card(deck) for _ in range(3)]
    spread_with_positions = [(card, card_position()) for card in spread]
    return spread_with_positions

# Örnek kullanım
if __name__ == "__main__":
    spread = three_card_spread(deck)
    print("3 Kartlık Yayılım (Geçmiş, Şimdi, Gelecek):")
    for idx, (card, position) in enumerate(spread):
        print(f"Kart {idx+1}: {card} ({position})")