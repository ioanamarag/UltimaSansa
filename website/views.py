from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Bon, Promotion
from . import db
import json
import os
import sqlite3
from sklearn.preprocessing import MinMaxScaler
import numpy as np


views = Blueprint('views', __name__)

categories_together = [[100, 87, 12, 45, 78], 
 [56, 100, 89, 65, 11], 
 [34, 67, 100, 19, 90], 
 [71, 33, 52, 100, 40], 
 [95, 26, 3, 88, 100]]

MEDIA_ROOT = os.path.join(os.getcwd(), "website","static")

@views.route('/', methods=['GET', 'POST'])
@login_required
def show_images():
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT sum(e1), sum(e2), sum(e3), sum(e4), sum(e5), sum(e6), sum(e7), sum(e8), sum(c1), sum(c2), sum(c3), sum(c4), sum(c5) from bon where id = ?", (current_user.id,))

    resulted_sums = list(cursor.fetchall()[0])

    resulted_sums = np.array(resulted_sums).reshape(-1,1)

    resulted_sums = MinMaxScaler().fit_transform(resulted_sums)

    cursor.execute("SELECT product_name, promo_type, price, e1, e2, e3, e4, e5, e6, e7, e8, c FROM promotion")

    rows = cursor.fetchall()

    list_with_recommandations = []

    for row in rows:
        product_name, promo_type, price, e1, e2, e3, e4, e5, e6, e7, e8, c = row
        points = resulted_sums[0] * e1 + resulted_sums[1] * e2 + resulted_sums[2] * e3 + resulted_sums[3] * e4 + resulted_sums[4] * e5 + resulted_sums[5] * e6 + resulted_sums[6] * e7 + resulted_sums[7] * e8
        together = categories_together[int(c[1])]
        together = np.array(together).reshape(-1,1)
        together = MinMaxScaler().fit_transform(together)
        for i in range(5):
            points += together[i] * resulted_sums[8 + i]
        
        list_with_recommandations.append([product_name, 'images/' + product_name.replace(" ", "-") + '.png', points, str(float(promo_type) * 100), price, str(round(price * (1 - float(promo_type)), 1))])

    list_with_recommandations = sorted(list_with_recommandations, key=lambda x: x[2])[:12]
    list_with_recommandations = [(a, b, d, e, f) for (a, b, c, d, e, f) in list_with_recommandations]

    print(list_with_recommandations)
        
    return render_template('home.html', images=list_with_recommandations, user=current_user)

