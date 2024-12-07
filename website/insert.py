import sqlite3
import os
import pandas as pd
import DateTime

conn = sqlite3.connect('instance/database.db')


cursor = conn.cursor()

file_path = os.path.join(os.getcwd(), "website/Users.xlsx")
data = pd.read_excel(file_path)
data_bon = pd.read_excel(os.path.join(os.getcwd(), 'website/Bon.xlsx'))
data_promotion = pd.read_excel(os.path.join(os.getcwd(), 'website/Promotion.xlsx'))

for _, row in data.iterrows():
       cursor.execute('''INSERT INTO user (id, email, password) VALUES (?, ?, ?)''', (row['id'], row['email'], row['password'])) 


for _, row in data_bon.iterrows():
    if isinstance(row['date'], pd.Timestamp):
        date_value = row['date'].strftime('%Y-%m-%d %H:%M:%S')  # Convert to string in 'YYYY-MM-DD HH:MM:SS' format
    else:
        date_value = row['date'] 
    cursor.execute('''INSERT INTO bon (id, user_id, date, e1, e2, e3, e4, e5, e6, e7, e8, c1, c2, c3, c4, c5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (row['id'], row['user_id'], str(row['date']), row['e1'], row['e2'], row['e3'], row['e4'], row['e5'], row['e6'], row['e7'], row['e8'], 
                    row['c1'], row['c2'], row['c3'], row['c4'], row['c5']))

for _, row in data_promotion.iterrows():
       cursor.execute('''INSERT INTO promotion (id, product_name, promo_type, price, e1, e2, e3, e4, e5, e6, e7, e8, c) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row['id'], row['product_name'], row['promo_type'], row['price'], row['e1'], row['e2'], row['e3'], row['e4'], row['e5'], row['e6'], row['e7'], row['e8'], row['c']))

conn.commit()


conn.close()

print("Data inserted successfully.")