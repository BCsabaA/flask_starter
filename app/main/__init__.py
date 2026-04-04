from flask import Blueprint

main_bp = Blueprint('main', __name__)

# Ezt kötelező ide a végére tenni, hogy a blueprint regisztrálja az útvonalakat
from . import routes