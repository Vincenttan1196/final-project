from project3.models import User, Post
from project3 import db


users = User.query.all()

#other options
User.query.first()
User.query.filter_by(username='Corey').all()
User.query.filter_by(username='Corey').first()
##

#other functions

#user = User.query.filter_by(username='Corey').first()
#print(user)

##

print(users)