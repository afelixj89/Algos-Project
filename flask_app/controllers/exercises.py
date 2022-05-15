from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.exercise import exercise
from flask_app.models.user import User



@app.route('/new')
def new_exercise():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new_exercise.html', user=User.get_by_id(data))


@app.route('/create/exercise', methods=['POST'])
def create_exercise():
    if 'user_id' not in session:
        return redirect('/logout')
    if not exercise.validate_exercises(request.form):
        return redirect('/new')
    data = {
        "exercise": request.form["exercise"],
        "date": request.form["date"],
        "weight":request.form["weight"],
        "sets": request.form["sets"],
        "reps": request.form["reps"],
        "time": request.form["time"],
        "speed": request.form["speed"],
        "level": request.form["level"],
        "user_id": session["user_id"]
    }
    exercise.save(data)
    return redirect('/db')


@app.route('/edit/exercise/<int:id>')
def edit_exercise(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("edit_exercise.html", edit=exercise.get_one(data), user=User.get_by_id(user_data))


@app.route('/update/exercise', methods=['POST'])
def update_exercise():
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        "exercise": request.form["exercise"],
        "date": request.form["date"],
        "weight": request.form["weight"],
        "sets": request.form["sets"],
        "reps": request.form["reps"],
        "time": request.form["time"],
        "speed": request.form["speed"],
        "level": request.form["level"],
        "user_id": session["user_id"]
    }
    exercise.update(data)
    return redirect('/db')


@app.route('/exercise/<int:id>')
def show_exercise(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    user_data = {
        "id": session['user_id']
    }
    return render_template("show_exercise.html", exercise=exercise.get_one(data), user=User.get_by_id(user_data))


@app.route('/destroy/exercise/<int:id>')
def destroy_exercise(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    exercise.destroy(data)
    return redirect('/db')
