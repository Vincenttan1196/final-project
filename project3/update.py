from project3.database import *
from project3.models import User

user = User.query.get(1)




db.session.commit()

