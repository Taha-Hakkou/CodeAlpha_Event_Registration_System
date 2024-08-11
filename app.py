#!/usr/bin/env python3
"""Flask Events App
"""
from flask import Flask, render_template, request, redirect, flash, jsonify
from db import DB
from models.registration import Registration

app = Flask(__name__)
db = DB()


@app.route('/', strict_slashes=False)
@app.route('/events', strict_slashes=False)
def events():
    """Renders list of events page
    """
    page = request.args.get('page')
    page = int(page) if page else 0
    events = db.get_events(page)
    return render_template('events.html', events=events)


@app.route('/events/<id>', strict_slashes=False)
def event(id):
    """Renders event details page
    """
    event = db.get_event(id)
    registered = db.db.registrations.find_one({'event_id': id})
    return render_template('event.html', event=event, registered=registered)


@app.route('/registrations', strict_slashes=False)
def registrations():
    """Renders list of registred events page
    """
    page = request.args.get('page')
    page = int(page) if page else 0
    events = db.get_registrations(page)
    return render_template('registrations.html', events=events)


@app.route('/registrations', methods=['POST'], strict_slashes=False)
def create_registration():
    """Creates a new registration instance
    """
    event_id = request.form.get('event_id')
    email = request.form.get('email')
    phone = request.form.get('phone')
    quantity = request.form.get('quantity')
    reg = Registration(event_id, quantity, email, phone)
    db.create_registration(reg)
    return redirect('/registrations')


@app.route('/registrations', methods=['DELETE'], strict_slashes=False)
def cancel_registration():
    """"""
    event_id = request.args.get('id')
    db.db.registrations.delete_one({'event_id': event_id})
    return jsonify({'message': 'registration successfully deleted'})


@app.route('/registrations/<id>', strict_slashes=False)
def registration(id):
    """Renders event registration page
    """
    registered_event = db.get_registration(id)
    event = db.get_event(id)
    return render_template('registration.html', event=event)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
