from base import db

class AdminVo(db.Model):

    __tablename__ = 'admin_table'
    admin_id = db.Column('admin_id', db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column('first_name', db.Text, nullable=False)
    middle_name = db.Column('middle_name', db.Text, nullable=False)
    last_name = db.Column('last_name', db.Text, nullable=False)
    user_name = db.Column('user_name', db.Text, nullable=False)
    password = db.Column('password', db.Text, nullable=False)
    date_of_birth = db.Column('date_of_birth', db.Text, nullable=False)

    def as_dict(self):
        return {
            'admin_id': self.admin_id,
            'first_name': self.first_name,
            'middle_name': self.middle_name,
            'last_name': self.last_name,
            'user_name': self.user_name,
            'password': self.password,
            'date_of_birth':  self.date_of_birth
        }


db.create_all()