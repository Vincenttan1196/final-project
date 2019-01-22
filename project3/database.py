from project3.models import *
from project3 import db
from sqlalchemy import desc

db.create_all()

users = User.query.order_by(User.score.desc()).all()

#RANK / ID / USERNAME /EMAIL / SCORE


score = db.session.query(User.rank, User.username, User.score)
#RANK/ USERNAME / SCORE


id = len(db.session.query(User.id).all())
rank = db.session.query(User.rank).all()
username = db.session.query(User.username).all()
scores = db.session.query(User.score).all()
db.session.commit()
test = User.query.order_by(User.score.desc()).first()
