"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personaje, Planeta, Personaje_favorito, Planeta_favorito
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/users', methods=['GET'])
def handle_users():
    try:
        response_body = ([{
            '_id': user.id,
            'name': user.nombre,
            'apellido': user.apellido,
            'email': user.email,
            'is_active': user.is_active,
        } for user in User.query.all()
        ])
        return jsonify(response_body), 200
    except Exception as e:
        print(f'Error /users: {e}')
        return (f'Error:/users {e}'), 500


@app.route('/users/favorites', methods=['GET'])
def handle_users_favorites():
    try:
        response_body = ([{
            '_id': user.id,
            'personajes': user.personajes,
            'planetas': user.planetas
        } for user in User.query.all()
        ])
        return jsonify(response_body), 200
    except Exception as e:
        print(f'ERROR users/favorites: {e}')
        return (f'ERROR users/favorites: {e}'), 500


@app.route('/people', methods=['GET'])
def handle_people():
    try:
        response_body = ([{
            '_id': personaje.id,
            'name': personaje.name,
            'height': personaje.height,
            'mass': personaje.mass,
            'hair_color': personaje.hair_color,
            'skin_color': personaje.skin_color,
            'eye_color': personaje.eye_color,
            'birth_year': personaje.birth_year,
            'gender': personaje.gender,
            'homeworld': personaje.homeworld,
            'created': personaje.created,
        } for personaje in Personaje.query.all()
        ])
        return jsonify(response_body), 200
    except Exception as e:
        print(f'Error: {e}')
        return (f'Error: {e}'), 500


@app.route('/people/<id>')
def get_people_id(id):
    print(id)
    try:
        personaje = Personaje.query.filter_by(id=id).first_or_404()
        return{
            'id': personaje.id,
            'name': personaje.nombre,
            'height': personaje.height,
            'mass': personaje.mass,
            'hair_color': personaje.hair_color,
            'skin_color': personaje.skin_color,
            'eye_color': personaje.eye_color,
            'birth_year': personaje.birth_year,
            'gender': personaje.gender,
            'homeworld': personaje.homeworld,
            'created': personaje.created,
        }
    except Exception as e:
        print(f'ERROR people/id: {e}')
        return (f'ERROR people/id: {e}'), 500


@app.route('/planet', methods=['GET'])
def handle_plenet():
    try:
        response_body = ([{
            '_id': planeta.id,
            'name': planeta.name,
            'orbital_period': planeta.orbital_period,
            'rotation_period': planeta.rotation_period,
            'diameter': planeta.diameter,
            'climate': planeta.climate,
            'gravity': planeta.gravity,
            'terrain': planeta.terrain,
            'surface_water': planeta.surface_water,
            'population': planeta.population,
            'created': planeta.created
        } for planeta in Planeta.query.all()
        ])
        return jsonify(response_body), 200
    except Exception as e:
        print(f'Error: {e}')
        return (f'Error: {e}'), 500


@app.route('/favorite/planet', methods=['POST'])
def handle_favorite_planet():
    try:
         usuario_id = request.json.get('usuario_id')
         planeta_id = request.json.get('planeta_id')
         planetaFavorio = Planeta_favorito(usuario_id=usuario_id, planeta_id = planeta_id)
         db.session.add(planetaFavorio)
         db.session.commit()
         return {
            'mensaje': 'ok'
        }, 200
    except Exception as e:
        print(f'new_user_ERROR: {e}')
        return 'ERROR', 500


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
