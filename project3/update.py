from project3.database import *
from project3.models import User
from project3.persistence import productInfo

second = User.query.get(4)
second.score = '10000'


db.session.commit()


print(second)

