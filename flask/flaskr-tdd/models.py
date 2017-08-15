from app import db


class Flaskr(db.Model):

    __tablename__ = "flaskr"

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, next):
        self.title = title
        self.next = next

    def __repr__(self, ):
        return '<title {}>'.format(self.body)
