from project3.database import *
from project3.models import User

user = User.query.get(1)
#user.ratings = 3

print(user._ratings[0])
print(user._ratings[2])
print(user._ratings[4])


db.session.commit()

