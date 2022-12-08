from flask import render_template, request, redirect # ADDED
from app import app
from models.event_list import events
from models.event import Event

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/events', methods = ['POST'])
def create():
    date = request.form["date"]
    name = request.form["name"]
    number_of_guests = request.form["number_of_guests"]
    location = request.form["location"]
    description = request.form["description"]
    # recurring = request.form["recurring"]
    new_event = Event(date, name, number_of_guests, location, description, True)
    events.append(new_event)
    # return render_template('index.html', title='Home', events=events)

    return redirect('/events')