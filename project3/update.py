from project3.database import *
from project3.models import User
from sqlalchemy import desc

second = User.query.get(3)
second.score = '1'
db.session.commit()


print(second)

