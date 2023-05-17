from flask import Blueprint, render_template, request


views = Blueprint('views',__name__)

@views.route("/")
def create_menu():
    return "<h1>Menu Page</h1>"