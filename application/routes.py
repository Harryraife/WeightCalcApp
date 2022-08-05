from flask import request, redirect, url_for, render_template
from application import app, db
from application.models import *
from application.forms import *
from datetime import date


@app.route('/', methods=['GET','POST'])
def home():
    return render_template('home.html')
    
#Create a new user    

@app.route('/add-lifter', methods = ['GET', 'POST'])
def add_lifter():
    message="Hi, If you are a new user then please supply your first and last name"
    form = NewUser()

    if request.method=='POST':
        if form.validate_on_submit():
            lifter = Lifter(
                first_name = form.first_name.data,
                last_name = form.last_name.data,
                username= form.username.data
            )
            db.session.add(lifter)
            db.session.commit()
            return redirect(url_for('view_all_users'))
    return render_template('add_lifter.html',form=form,message=message)

#Create a new entry in the log

@app.route('/add-lift', methods = ['GET','POST'])
def add_lift():
    message = "Please input your weight, reps completed and the exercise which you completed"
    form = NewLift()
    lifters = Lifter.query.all()
    form.user.choices = [(lifter.username, f"{lifter.username}") for lifter in lifters]
    if request.method == 'POST':
        if form.validate_on_submit():
            log = Log(
                date = form.date.data,
                weight = form.weight.data,
                reps = form.reps.data,
                exercise = form.lift.data,
                lifter_id = form.user.data
            )
            db.session.add(log)
            db.session.commit()
            return redirect(url_for('logs'))
    return render_template('add_lift.html',form=form, message = message)

#Read the whole of the log list

@app.route('/view-lifts', methods = ['GET'])
def logs():
    all_lifts = Log.query.all()
    return render_template('view_all.html', entity='Log', log=Log, all_lifts=all_lifts)

#Read all the users in the database

@app.route('/view-lifters')
def view_all_users():
    users = Lifter.query.all()
    return render_template('view_all.html', entity='User', all_lifts=users)

#Update the name of a user

@app.route('/update-lifter/<int:id>', methods = ['GET', 'POST'])
def update_lifter(id):
    lifter_to_update = Lifter.query.get(id)
    form = NewUser()
    if form.validate_on_submit():
        first_name, last_name, username = form.first_name.data, form.last_name.data, form.username.data
        lifter_to_update.first_name = first_name
        lifter_to_update.last_name = last_name
        lifter_to_update.username = username
        db.session.commit()
        return redirect(url_for('view_all_users'))
    form.first_name.data = lifter_to_update.first_name
    form.last_name.data = lifter_to_update.last_name
    form.username.data = lifter_to_update.username
    return render_template('add_lifter.html', form=form)

#Update a lift already logged

@app.route('/update-lift/<int:id>', methods=['GET', 'POST'])
def update_lift(id):
    lift_to_update = Log.query.get(id)
    form = NewLift()
    lifters = Lifter.query.all()
    form.user.choices = [(lifter.username, f"{lifter.username}") for lifter in lifters]
    if form.validate_on_submit():
        lift_to_update.date = form.date.data
        lift_to_update.weight = form.weight.data
        lift_to_update.reps = form.reps.data
        lift_to_update.exercise = form.lift.data
        db.session.commit()
        return redirect(url_for('logs'))
    form.lift.data = lift_to_update.exercise
    form.reps.data = lift_to_update.reps
    form.weight.data = lift_to_update.weight
    form.date.data = lift_to_update.date
    return render_template('add_lift.html', form=form)

#Delete a lifter in the database

@app.route('/delete-lifter/<int:id>')
def delete_lifter(id):
    lifter_to_delete = Lifter.query.get(id)
    db.session.delete(lifter_to_delete)
    db.session.commit()
    return redirect(url_for('view_all_users'))

#delete a log in the activity database

@app.route('/delete-lift/<int:id>')
def delete_lift(id):
    lift_to_delete = Log.query.get(id)
    db.session.delete(lift_to_delete)
    db.session.commit()
    return redirect(url_for('logs'))    