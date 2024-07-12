from flask import Blueprint
from .api import  *


home_app = Blueprint("home_app", __name__)


homepage_view = HomePageAPI.as_view('homepage_api')

home_app.add_url_rule('/', 
	view_func=homepage_view, 
	methods=['POST','GET'])
