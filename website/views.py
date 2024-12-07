from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import BonClick, Promotion
from . import db
import json
import os

views = Blueprint('views', __name__)

MEDIA_ROOT = os.path.join(os.getcwd(), "website/static")

@views.route('/', methods=['GET', 'POST'])
@login_required
def show_images():
    image_folder = os.path.join(MEDIA_ROOT, 'images')
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'png', 'jpeg', 'gif'))]
    image_paths = [os.path.join('images', img) for img in image_files]
    return render_template('home.html', images=image_paths, user=current_user)

