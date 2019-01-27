from project3.database import *
from project3.models import User

user = User.query.get(1)
user.ratings = 3
user.ratings = 1
user.ratings = 5

db.session.commit()

