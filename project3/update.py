from project3.database import *
from project3.models import User
from sqlalchemy import desc

second = User.query.get(1)
second.score = '123'
db.session.commit()


print(second)

