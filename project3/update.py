from project3.database import *

second = User.query.get(2)
second.score = '2'
db.session.commit()

print(second)
print(second.score)