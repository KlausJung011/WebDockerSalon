from . import db
from datetime import datetime


class Salon(db.Model):
    __tablename__ = 'salones'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    disponible = db.Column(db.Boolean, default=True)
    reservas = db.relationship('Reserva', backref='salon', lazy=True)

    def __repr__(self):
        return f'<Salon {self.nombre}>'


class Evento(db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    capacidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    reservas = db.relationship('Reserva', backref='evento', lazy=True)

    def __repr__(self):
        return f'<Evento {self.nombre}>'


class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(120), nullable=False)
    contacto = db.Column(db.String(150), nullable=False)
    fecha_evento = db.Column(db.String(20), nullable=False)
    salon_id = db.Column(db.Integer, db.ForeignKey('salones.id'), nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'), nullable=False)
    fecha_reserva = db.Column(db.DateTime, default=datetime.utcnow)
    notas = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Reserva {self.cliente}>'
