import app

db = app.db


class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(45), primary_key=True)
    full_name = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True)
    is_admin = db.Column(db.Boolean)
    picture_url = db.Column(db.String(200))
    receive_notifications = db.Column(db.Boolean, default=True, server_default="True", nullable=False)
    leagues_won = db.Column(db.Integer, nullable=False, default=0, server_default="0")
    teams = db.relationship('PlayerTeamModel')

    def __init__(self, user_id, full_name, email, picture_url):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.is_admin = False
        self.picture_url = picture_url

    def __repr__(self):
        return '<User {}>'.format(self.full_name)

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def find_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    def json(self):
        return {
            'user_id': self.user_id,
            'full_name': self.full_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'picture_url': self.picture_url,
            'receive_notifications': self.receive_notifications,
            'teams': [team.json_for_user() for team in self.teams],
            'leagues_won': self.leagues_won
        }

    def json_user_owner_basic(self):
        return {
            'user_id': self.user_id,
            'full_name': self.full_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'picture_url': self.picture_url,
            'receive_notifications': self.receive_notifications,
            'leagues_won': self.leagues_won
        }

    def user_json(self):
        return {
            'user_id': self.user_id,
            'full_name': self.full_name,
            'email': self.email,
            'is_admin': self.is_admin,
            'picture_url': self.picture_url,
            'leagues_won': self.leagues_won
        }

    def upsert(self):
        db.session.add(self)
        db.session.commit()
