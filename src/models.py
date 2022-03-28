from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    fecha_subscripcion = db.Column(db.String(100))
    personajes = db.relationship('Personaje', lazy=True) 
    planetas = db.relationship('Planeta', lazy=True)

    def __init__(self,id,nombre,apellido,email,password,fecha_subscripcion,is_active,personajes, planetas):
        self.id= id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        self.fecha_subscripcion = fecha_subscripcion
        self.is_active = is_active
        self.personajes = personajes
        self.planetas = planetas

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "appellido": self.apellido,
            "email": self.email,
            "password": self.password,
            "fecha_subscripcion": self.fecha_subscripcion,
            "is_active": self.is_active,
            "personajes" : list(map(lambda x: x.serialize(), self.personajes)),
            "planetas" : list(map(lambda x: x.serialize(), self.planetas))

        }



# class Usuario(db.Model):
    # __tablename__ = 'usuario'
    # id = db.Column(db.Integer, primary_key=True)
    # nombre = db.Column(db.String(100))
    # apellido = db.Column(db.String(100))
    # email = db.Column(db.String(150))
    # password = db.Column(db.String(150))
    # fecha_subscripcion = db.Column(db.String(100))
    # personajes = db.relationship('Personaje', lazy=True) 
    # planetas = db.relationship('Planeta', lazy=True)

    # def __init__(self,nombre,apellido,email,password,fecha_subscripcion,personaje, planeta):
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.email = email
    #     self.password = password
    #     self.fecha_subscripcion = fecha_subscripcion
    #     self.personajes = personajes
    #     self.planetas = planetas

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "nombre": self.nombre,
    #         "appellido": self.apellido,
    #         "email": self.email,
    #         "password": self.password,
    #         "fecha_subscripcion": self.fecha_subscripcion,
    #         "personajes" : list(map(lambda x: x.serialize(), self.personajes)),
    #         "planetas" : list(map(lambda x: x.serialize(), self.planetas))

    #     }


class Personaje(db.Model):
    __tablename__ = 'personaje'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    height = db.Column(db.String(100))
    mass = db.Column(db.String(100))
    hair_color = db.Column(db.String(100))
    skin_color = db.Column(db.String(100))
    eye_color = db.Column(db.String(100))
    birth_year = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    homeworld = db.Column(db.String(150))
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    #usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=False, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self,name,height,mass,hair_color,skin_color,eye_color,birth_year,gender,homeworld,created):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.created = created

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "appellido": self.apellido,
            "email": self.email,
            "password": self.password,
            "fecha_subscripcion": self.fecha_subscripcion
        }

class Personaje_favorito(db.Model):
    __tablename__ = 'personaje_favorito'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    personaje_id = db.Column(db.Integer,db.ForeignKey('personaje.id'))

    def __init__(self, usuario_id, personaje_id):
        self.usuario_id = usuario_id
        self.personaje_id = personaje_id

    def __repr__(self):
        return '<Personaje_favorito %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.usuario_id,
            "id_personaje": self.personaje_id
        }
# class Personaje_favorito(db.Model):
#     __tablename__ = "personaje_favorito"
#     id = db.Column(db.Integer, primary_key=True)
#     notes = db.Column(db.String(100), nullable=True)
#     usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
#     personaje_id = db.Column(db.Integer, db.ForeignKey('personaje.id'))



class Planeta(db.Model):
    __tablename__ = 'planeta'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    orbital_period = db.Column(db.String(100))
    rotation_period = db.Column(db.String(100))
    diameter = db.Column(db.String(100))
    climate = db.Column(db.String(100))
    gravity = db.Column(db.String(100))
    terrain = db.Column(db.String(100))
    surface_water = db.Column(db.String(100))
    population = db.Column(db.String(100))
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    #usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=False, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self,name,orbital_period,rotation_period,diameter,climate,gravity,terrain,surface_water,
    population,created,usuarios):
        self.name=name
        self.orbital_period= orbital_period
        self.rotation_period = rotation_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.surface_water = surface_water
        self.population = population
        self.created = created
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diamteter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
            "created": self.created
        }

class Planeta_favorito(db.Model):
    __tablename__ = 'planeta_favorito'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    planeta_id = db.Column(db.Integer,db.ForeignKey('planeta.id'))

    def __init__(self, usuario_id, planeta_id):
        self.usuario_id = usuario_id
        self.planeta_id = planeta_id

    def __repr__(self):
        return '<Planeta_favorito %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "id_usuario": self.usuario_id,
            "id_planeta": self.planeta_id
        }
# class Planeta_favorito(db.Model):
#     __tablename__ = "planeta_favorito"
#     id = db.Column(db.Integer, primary_key=True)
#     notes = db.Column(db.String(100), nullable=True)
#     usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
#     planeta_id = db.Column(db.Integer, db.ForeignKey('planeta.id'))