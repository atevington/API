import app
from .game import  GameModel
db = app.db


class LeagueModel(db.Model):
    __tablename__ = 'leagues'

    league_id = db.Column(db.Integer, nullable=False, primary_key=True)
    league_name = db.Column(db.String(50), nullable=False)
    league_description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    teams = db.relationship("PlayerTeamModel")

    def __init__(self, league_name, league_description, price):
        self.league_name = league_name
        self.league_description = league_description
        self.price = price

    def json(self):
        price = self.price / 100
        return {
            'league_id': self.league_id,
            'league_name': self.league_name,
            'league_description': self.league_description,
            'price': "{:,.2f}".format(price),
            'current_week': GameModel.get_max_week(),
            'teams': [team.json_basic() for team in self.teams]
        }

    def json_league_info(self):
        price = self.price / 100
        return {
            'league_id': self.league_id,
            'league_name': self.league_name,
            'league_description': self.league_description,
            'price': "{:,.2f}".format(price),
        }

    def upsert(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_league_by_id(cls, league_id):
        return cls.query.filter_by(league_id=league_id).first()

    @classmethod
    def find_all_leagues(cls):
        return cls.query.all()
