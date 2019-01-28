from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from project3 import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Score(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    score = db.Column(db.Integer, default=0)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    score = db.Column(db.Integer,default = 0)
    rank = db.Column(db.Integer, default=1)
    #Immanuel
    budget = db.Column(db.Integer, default=0)
    food = db.Column(db.Integer, default=0)
    grocery = db.Column(db.Integer, default=0)
    entertainment = db.Column(db.Integer, default=0)
    luxury = db.Column(db.Integer, default=0)
    others = db.Column(db.Integer, default=0)
    #Jonathan
    electricity = db.Column(db.Integer, default=0)
    water = db.Column(db.Integer, default=0)
    billothers = db.Column(db.Integer, default=0)
    #Vincent
    _ratings = db.Column(db.String, default='0')

    @property
    def ratings(self):
        return [float(x) for x in self._ratings.split(',')]

    @ratings.setter
    def ratings(self, value):
        self._ratings += ',%s' % value



    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('ID-{self.id},USERNAME-{self.username},'EMAIL-{self.email}',SCORE-{self.score}, " \
               f"BUDGET-{self.budget}, ELECTRICITY-{self.electricity}, WATER-{self.water},OTHERS-{self.billothers},RATINGS-{self._ratings} "


    #def __repr__(self):
        #return f"User('USERNAME-{self.username}', 'EMAIL-{self.email}', '{self.image_file}' )"




