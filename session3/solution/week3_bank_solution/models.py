from config import db


class Account(db.Model):
    __tablename__ = 'user_account'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    balance = db.Column(db.Integer, default=0)
    svg = db.relationship('Savings', uselist=False,
                          backref='savings', cascade="all,delete")


class Savings(db.Model):
    __tablename__ = 'savings'
    id = db.Column(db.Integer, primary_key=True)
    saving_balance = db.Column(db.Integer, nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey(
        'user_account.id'), nullable=False)
