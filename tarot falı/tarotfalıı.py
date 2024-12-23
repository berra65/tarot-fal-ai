import sqlite3

# Veritabanı bağlantısı oluşturun
conn = sqlite3.connect('tarot.db')
c = conn.cursor()

# Kartlar tablosunu oluşturun
c.execute('''
          CREATE TABLE IF NOT EXISTS cards (
              name TEXT PRIMARY KEY,
              upright_meaning TEXT,
              reversed_meaning TEXT,
              categories TEXT
          )
          ''')

# Veritabanı bağlantısını kapatın
conn.commit()
conn.close()

print("Veritabanı ve tablo başarıyla oluşturuldu.")
