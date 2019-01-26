from project3.database import *
from project3.models import User
from sqlalchemy import desc

second = User.query.get(4)
second.score = '10000'
db.session.commit()


print(second)

