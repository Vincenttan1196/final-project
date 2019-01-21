from project3.models import User
from project3 import db

db.create_all()

users = User.query.all()


db.session.commit()

#ID / USERNAME / SCORE

print(users)


