from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'neojardin-secret-2024'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neojardin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()
        seed_data()

    return app


def seed_data():
    from .models import Salon, Evento, Reserva
    if Salon.query.count() == 0:
        salones = [
            Salon(nombre='Salón Cristal', capacidad=200, descripcion='Espacio luminoso con paredes de vidrio y vista al jardín. Ideal para bodas y galas.', disponible=True),
            Salon(nombre='Sala Ébano', capacidad=80, descripcion='Ambiente íntimo con decoración en madera oscura. Perfecto para cenas corporativas.', disponible=True),
            Salon(nombre='Terraza Aurora', capacidad=150, descripcion='Terraza al aire libre con iluminación ambiental y vista panorámica de la ciudad.', disponible=True),
            Salon(nombre='Salón Imperial', capacidad=350, descripcion='Nuestro espacio más grande y lujoso, equipado con sistema de sonido y pantallas LED.', disponible=False),
        ]
        db.session.add_all(salones)

    if Evento.query.count() == 0:
        eventos = [
            Evento(nombre='Gala de Negocios 2025', descripcion='Noche de networking y elegancia para líderes empresariales de la región.', capacidad=180, precio=1500.00),
            Evento(nombre='Boda Etérea', descripcion='Celebración nupcial con decoración floral y música en vivo.', capacidad=200, precio=4500.00),
            Evento(nombre='Cumpleaños VIP', descripcion='Celebración exclusiva con cóctel de bienvenida y espectáculo de luces.', capacidad=80, precio=900.00),
            Evento(nombre='Congreso Innovación', descripcion='Evento académico y empresarial con ponentes internacionales.', capacidad=300, precio=2000.00),
        ]
        db.session.add_all(eventos)
        db.session.commit()
