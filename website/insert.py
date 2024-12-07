import sqlite3
import os
import pandas as pd

conn = sqlite3.connect('instance/database.db')

cursor = conn.cursor()

file_path = os.path.join(os.getcwd(), "website/Users.xlsx")
data = pd.read_excel(file_path)
data_bonclick = pd.read_excel(os.path.join(os.getcwd(), 'website/BonClick.xlsx'))
data_promotions = pd.read_excel(os.path.join(os.getcwd(), 'website/Promotions.xlsx'))

for _, row in data.iterrows():
       cursor.execute('''INSERT INTO user (id, email, password) VALUES (?, ?, ?)''', (row['id'], row['email'], row['password'])) 

for _, row in data_bonclick.iterrows():
       cursor.execute('''INSERT INTO user (id, user_id, date, e1, e2, e3, e4, e5, e6, e7, e8, c1, c2, c3, c4, c5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['id'], row['user_id'], row['date'], row['e1'], row['e2'], row['e3'], row['e4'], row['e5'], row['e6'], row['e7'], row['e8'], row['c1'], row['c2'], row['c3'], row['c4'], row['c5']))  

for _, row in data_promotions.iterrows():
       cursor.execute('''INSERT INTO user (id, product_name, promo_type, e1, e2, e3, e4, e5, e6, e7, e8, c) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['id'], row['product_name'], row['promo_type'], row['e1'], row['e2'], row['e3'], row['e4'], row['e5'], row['e6'], row['e7'], row['e8'], row['c']))

conn.commit()

conn.close()

print("Data inserted successfully.")