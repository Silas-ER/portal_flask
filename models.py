from app import db

class Usuarios(db.Model):
    nickname = db.Column(db.String(10), primary_key=True)
    senha = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
