from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from . import db
from .models import Salon, Evento, Reserva

main = Blueprint('main', __name__)


# ─── HOME ────────────────────────────────────────────────────────────────────
@main.route('/')
def index():
    salones = Salon.query.all()
    eventos = Evento.query.all()
    total_reservas = Reserva.query.count()
    return render_template('index.html', salones=salones, eventos=eventos, total_reservas=total_reservas)


# ─── SALONES ─────────────────────────────────────────────────────────────────
@main.route('/salones')
def salones():
    salones = Salon.query.all()
    return render_template('salones.html', salones=salones)


@main.route('/salones/editar/<int:id>', methods=['GET', 'POST'])
def editar_salon(id):
    salon = Salon.query.get_or_404(id)
    if request.method == 'POST':
        salon.nombre = request.form['nombre']
        salon.capacidad = int(request.form['capacidad'])
        salon.descripcion = request.form['descripcion']
        salon.disponible = 'disponible' in request.form
        db.session.commit()
        flash('Salón actualizado correctamente.', 'success')
        return redirect(url_for('main.salones'))
    return render_template('editar_salon.html', salon=salon)


# ─── EVENTOS ─────────────────────────────────────────────────────────────────
@main.route('/eventos')
def eventos():
    eventos = Evento.query.all()
    return render_template('eventos.html', eventos=eventos)


# ─── RESERVAS ────────────────────────────────────────────────────────────────
@main.route('/reservas')
def reservas():
    reservas = Reserva.query.order_by(Reserva.fecha_reserva.desc()).all()
    return render_template('reservas.html', reservas=reservas)


@main.route('/reservas/nueva', methods=['GET', 'POST'])
def nueva_reserva():
    salones = Salon.query.filter_by(disponible=True).all()
    eventos = Evento.query.all()
    if request.method == 'POST':
        reserva = Reserva(
            cliente=request.form['cliente'],
            contacto=request.form['contacto'],
            fecha_evento=request.form['fecha_evento'],
            salon_id=int(request.form['salon_id']),
            evento_id=int(request.form['evento_id']),
            notas=request.form.get('notas', '')
        )
        db.session.add(reserva)
        db.session.commit()
        flash('¡Reserva creada exitosamente!', 'success')
        return redirect(url_for('main.reservas'))
    return render_template('nueva_reserva.html', salones=salones, eventos=eventos)


@main.route('/reservas/eliminar/<int:id>', methods=['POST'])
def eliminar_reserva(id):
    reserva = Reserva.query.get_or_404(id)
    db.session.delete(reserva)
    db.session.commit()
    flash('Reserva eliminada.', 'info')
    return redirect(url_for('main.reservas'))


# ─── API JSON ─────────────────────────────────────────────────────────────────
@main.route('/api/stats')
def api_stats():
    return jsonify({
        'salones': Salon.query.count(),
        'eventos': Evento.query.count(),
        'reservas': Reserva.query.count(),
        'salones_disponibles': Salon.query.filter_by(disponible=True).count()
    })
