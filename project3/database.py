from project3.models import User, Score
from project3 import db
from sqlalchemy import desc

db.create_all()

users = User.query.all()
#RANK / ID / USERNAME /EMAIL / SCORE


score = db.session.query(User.rank, User.username, User.score)
#RANK/ USERNAME / SCORE

rank = db.session.query(User.rank).all()
username = db.session.query(User.username).all()
scores = db.session.query(User.score).all()

db.session.commit()

print(users)
