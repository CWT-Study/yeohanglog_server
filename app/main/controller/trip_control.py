from flask import Blueprint, request

import app.main.service.user_service as user_service
from app.main.model.response_model import get_response

trip_blueprint = Blueprint("trip", __name__, url_prefix="/TripLog/trip")

