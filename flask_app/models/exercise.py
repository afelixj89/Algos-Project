from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user



class exercise:
    db_name = "exercises"

    def __init__(self, db_data):
        self.id = db_data['id']
        self.exercise = db_data['exercise']
        self.sets = db_data['sets']
        self.weight = db_data['weight']
        self.level = db_data['level']
        self.date = db_data['date']
        self.reps = db_data['reps']
        self.time = db_data['time']
        self.speed = db_data['speed']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data["user_id"]
        self.user = ["user"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO exercises (exercise, sets, weight, level, date, reps, time, speed, user_id) VALUES (%(exercise)s,%(sets)s,%(weight)s,%(level)s,%(date)s,%(reps)s,%(time)s,%(speed)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM exercises;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_exercises = []
        for row in results:
            all_exercises.append(cls(row))
        return all_exercises
        

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM exercises WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_one_by_user(cls, data):
        query = "SELECT * FROM exercises WHERE user_id = %(user_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE exercises SET %(exercise)s,%(sets)s,%(weight)s,%(level)s,%(date)s,%(reps)s,%(time)s,%(speed)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM exercises WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_exercises(exercises):
        is_valid = True
        if len(exercises['exercise']) < 3:
            is_valid = False
            flash("Exercise Name must be at least 3 characters", "exercises")
        if len(exercises['date']) < 3:
            is_valid = False
            flash("Date must be entered", "exercises")
        # if int(exercises['weight']) < 1:
        #     is_valid = False
        #     flash("weight must be a greater than 0", "exercises")
        # if (exercises['weight']) != int:
        #     is_valid = False
        #     flash("Weight must be numerical ", "exercises")
        # if len(exercises['exercise']) < 3:
        #     is_valid = False
        #     flash("Exercise Name must be at least 3 characters", "exercises")
        # if len(exercises['date']) < 3:
        #     is_valid = False
        #     flash("Date must be entered", "exercises")
        # if len(exercises['weight']) < 2:
        #     is_valid = False
        #     flash("Weight must be over two digits ", "exercises")
        # NEED HELP WITH VALIDATING INT
        return is_valid
