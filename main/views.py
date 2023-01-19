from flask import Flask, Blueprint, jsonify
from main.dao.netflix_dao import NetflixDAO
import json

instance_neflix_dao = NetflixDAO('netflix.db')

main = Blueprint('main', __name__)

# view to display a list of movies by title


@main.route('/movie/<title>')
def movie_by_title(title):
    data_by_title = instance_neflix_dao.qury_data_by_title(title)
    return jsonify(data_by_title)

# view to display a list of movies by range of years


@main.route('/movie/<first_year>/to/<second_year>')
def year_to_year(first_year, second_year):
    data_by_years = instance_neflix_dao.query_year_to_year(first_year, second_year)
    return jsonify(data_by_years)

# view to display a list of movies by age marker


@main.route('/rating/children')
def qury_rating_children():
    data_by_rating = instance_neflix_dao.query_rating('children')
    return jsonify(data_by_rating)

# view to display a list of movies by age marker


@main.route('/rating/family')
def qury_rating_family():
    data_by_rating = instance_neflix_dao.query_rating('family')
    return jsonify(data_by_rating)

# view to display a list of movies by age marker


@main.route('/rating/adult')
def qury_rating_adult():
    data_by_rating = instance_neflix_dao.query_rating('adult')
    return jsonify(data_by_rating)

# view to display a list of movies by genre


@main.route('/genre/<genre>')
def qury_by_genre(genre):
    data_by_rating = instance_neflix_dao.query_by_genre(genre)
    return jsonify(data_by_rating)