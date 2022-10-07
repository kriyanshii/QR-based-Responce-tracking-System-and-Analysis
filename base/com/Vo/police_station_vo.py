from base import db

class PoliceStationVo(db.Model):

    __tablename__ = 'police_stations_table'
    police_station_id = db.Column('police_station_id', db.Integer, primary_key=True, autoincrement=True)
    police_station_name = db.Column('police_station_name', db.Text, nullable=False)
    lane_1 = db.Column('lane_1', db.Text, nullable=False)
    lane_2 = db.Column('lane_2', db.Text, nullable=True)
    district = db.Column('district', db.Text, nullable=False)
    state = db.Column('state', db.Text, nullable=False)

    def as_dict(self):
        return {
            'police_station_id': self.police_station_id,
            'police_station_name': self.police_station_name,
            'lane_1': self.lane_1,
            'lane_2': self.lane_2,
            'district': self.district,
            'state': self.state,
        }


db.create_all()