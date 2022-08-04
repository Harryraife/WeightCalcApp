from application import db 

class Lifter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    username = db.Column(db.String(30), nullable = False)
    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name}. their username is {self.username}"

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, nullable = False)
    reps = db.Column(db.Integer, nullable = False)
    exercise = db.Column(db.String(10), nullable = False)
    date = db.Column(db.Date)
    lifter_id = db.Column(db.Integer, db.ForeignKey('lifter.id'), nullable = False)
    def __str__(self):
        return f"{self.id}: {self.lifter_id} completed {self.reps} {self.exercise} reps @{self.weight}kg on {self.date}"

class Max(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(10), nullable = False)
    max = db.Column(db.Integer, nullable = False)
    predicted = db.Column(db.Boolean) 
    lifter_id = db.Column(db.Integer, db.ForeignKey('lifter.id'), nullable = False)

