import sqlite3
import json

# JSON verisini yükleyin
with open('c:\\Users\\MESUT DENİZ\\OneDrive\\Masaüstü\\tarot falı\\tarot_cards.json', 'r', encoding='utf-8') as f:
    tarot_cards = json.load(f)

# Veritabanı bağlantısı oluşturun
conn = sqlite3.connect('tarot.db')
c = conn.cursor()

# 'cards' tablosunu oluşturun (eğer yoksa)
c.execute('''
CREATE TABLE IF NOT EXISTS cards (
    name TEXT PRIMARY KEY,
    upright_meaning TEXT,
    reversed_meaning TEXT,
    categories TEXT
)
''')

# Kartları veritabanına ekleyin
for card in tarot_cards:
    c.execute('''
              INSERT OR REPLACE INTO cards (name, upright_meaning, reversed_meaning, categories)
              VALUES (?, ?, ?, ?)
              ''', (card['name'], card['upright_meaning'], card['reversed_meaning'], json.dumps(card['categories'])))

# Değişiklikleri kaydedin ve veritabanı bağlantısını kapatın
conn.commit()
conn.close()

print("Kartlar başarıyla veritabanına eklendi.")

# Kart bilgilerini getiren fonksiyon
def get_card_data(card_name):
    conn = sqlite3.connect('tarot.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cards WHERE name=?', (card_name,))
    card = c.fetchone()
    conn.close()
    return card

# Örnek kullanım
card_data = get_card_data('Aşıklar')
print(card_data)
