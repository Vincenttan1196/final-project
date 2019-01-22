from project3.database import *
from project3.models import User
from sqlalchemy import desc

second = User.query.get(2)
second.score = '2'
db.session.commit()

print(second)
print(second.score)

all = User.query.all()

