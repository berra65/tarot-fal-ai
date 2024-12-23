from logic.draw_cards.py import three_card_spread # type: ignore
from logic.interpret_cards import interpret_cards

def main():
    # Kullanıcıdan niyet veya soru alın
    user_query = input("Lütfen niyetinizi veya sorunuzu yazın: ")
    keywords = user_query.split()  # Basit anahtar kelime çıkarma

    # Kartları çekin
    deck = [
        "Deli", "Büyücü","Başrahibe","İmparatoriçe","İmparator","Aziz","Aşıklar","Savaş Arabası","Güç","Ermiş","Kader Çarkı","Adalet","Asılan Adam","Ölüm","Denge","Şeytan","Kule","Yıldız",
"Ay","Güneş","Mahkeme","Dünya","As Kupa","İkili Kupa","Üçlü Kupa","Dörtlü Kupa","Beşli Kupa","Altılı Kupa","Yedili Kupa","Sekizli Kupa","Dokuzlu Kupa","Onlu Kupa","Vale Kupa",
"Şövalye Kupa","Kraliçe Kupa","Kral Kupa","As Kılıç","İkili Kılıç","Üçlü Kılıç","Dörtlü Kılıç","Beşli Kılıç","Altılı Kılıç","Yedili Kılıç","Sekizli Kılıç","Dokuzlu Kılıç","Onlu Kılıç",
"Vale Kılıç","Şövalye Kılıç","Kraliçe Kılıç","Kral Kılıç","As Değnek","İkili Değnek","Üçlü Değnek","Dörtlü Değnek","Beşli Değnek","Altılı Değnek","Yedili Değnek","Sekizli Değnek",
"Dokuzlu Değnek","Onlu Değnek","Vale Değnek","Şövalye Değnek","Kraliçe Değnek","Kral Değnek","As Para","İkili Para","Üçlü Para","Dörtlü Para","Beşli Para","Altılı Para","Yedili Para",
"Sekizli Para","Dokuzlu Para","Onlu Para","Vale Para","Şövalye Para","Kraliçe Para","Kral Para"
]
    
    spread = three_card_spread(deck)

    # Kartları yorumlayın
    interpretations = interpret_cards(spread, keywords)
    for interp in interpretations:
        print(interp)

if __name__ == "__main__":
    main()