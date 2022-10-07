from base import db
from base.com.Vo.police_station_vo import PoliceStationVo

class PoliceStationDao:

    def insert_ps(self,police_station_vo):
        db.session.add(police_station_vo)
        db.session.commit()

    def view_ps(self):
        ps_list = PoliceStationVo.query.all()
        return ps_list

    def delete_ps(self,police_station_vo):
        ps_list = PoliceStationVo.query.get(police_station_vo)
        db.session.delete(ps_list)
        db.session.commit()

    def edit_ps(self,police_station_vo):
        return PoliceStationVo.query.get(police_station_vo)

    def update_ps(self,police_station_vo):
        police_station = PoliceStationVo.query.get(police_station_vo.police_station_id)
        police_station.police_station_name = police_station_vo.police_station_name
        police_station.lane_1 = police_station_vo.lane_1
        police_station.lane_2 = police_station_vo.lane_2
        police_station.district = police_station_vo.district
        police_station.state = police_station_vo.state
        db.session.commit()