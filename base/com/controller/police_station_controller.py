from flask import *
from  base import app
from base.com.Dao.police_station_dao import PoliceStationDao
from base.com.Vo.police_station_vo import PoliceStationVo

app.secret_key = "khjasBDHJSGFJdsbfebaueiEU73gh714jaskg87Cabdjsajdb"

@app.route("/admin/load_police_station_registration")
def load_police_station_registration():

    police_station_vo = PoliceStationVo()
    police_station_dao = PoliceStationDao()

    ps_list = police_station_dao.view_ps()

    return render_template("/admin/police_station_add.html",ps_list=ps_list)

@app.route("/admin/police_station_add",methods=["POST"])
def police_station_add():

    police_staion_name = request.form.get("ps_name")
    lane_1 = request.form.get("lane_1")
    lane_2 = request.form.get("lane_2")
    district = request.form.get("district")
    state = request.form.get("state")

    police_station_vo = PoliceStationVo()
    police_station_dao = PoliceStationDao()

    ps_list = police_station_dao.view_ps()
    ps_name_list = [i.as_dict()['police_station_name'] for i in ps_list]

    if police_staion_name in ps_name_list:
        flash("Police Station Name already exist!!")
        ps_list = police_station_dao.view_ps()
        return render_template("/admin/police_station_add.html",ps_list=ps_list)

    police_station_vo.police_station_name = police_staion_name
    police_station_vo.lane_1 = lane_1
    police_station_vo.lane_2 = lane_2
    police_station_vo.district = district
    police_station_vo.state = state

    police_station_dao.insert_ps(police_station_vo)

    return redirect("/admin/load_police_station_registration")

@app.route("/admin/police_station_view")
def police_station_view():

    police_station_dao = PoliceStationDao()
    ps_list = police_station_dao.view_ps()

    return render_template("/admin/police_station_view.html",ps_list=ps_list)

@app.route("/admin/police_station_delete")
def police_station_delete():

    police_station_vo = PoliceStationVo()
    police_station_dao = PoliceStationDao()

    police_station_id = request.args.get("id")

    police_station_vo.police_station_id = police_station_id
    police_station_dao.delete_ps(police_station_vo.police_station_id)

    return redirect("/admin/load_police_station_registration")

@app.route("/admin/police_station_edit")
def police_station_edit():

    police_station_vo = PoliceStationVo()
    police_station_dao = PoliceStationDao()

    police_station_vo.police_station_id = request.args.get("id")
    id_list = police_station_dao.edit_ps(police_station_vo.police_station_id)

    return render_template("/admin/police_station_update.html",id_list=id_list)

@app.route("/admin/police_station_update",methods=["POST"])
def police_station_update():

    police_staion_id = request.form.get("id")
    police_staion_name = request.form.get("ps_name")
    lane_1 = request.form.get("lane_1")
    lane_2 = request.form.get("lane_2")
    district = request.form.get("district")
    state = request.form.get("state")

    police_station_vo = PoliceStationVo()
    police_station_dao = PoliceStationDao()

    ps_list = police_station_dao.view_ps()
    ps_name_list = [i.as_dict()['police_station_name'] for i in ps_list]
    ps_id_list = [i.as_dict()['police_station_id'] for i in ps_list]

    print(ps_id_list)
    index = ps_id_list.index(int(police_staion_id))

    if police_staion_name != ps_name_list[index] and police_staion_name in ps_name_list:
        flash("Police Station Name already exist!!")
        return redirect("/admin/police_station_edit")

    police_station_vo.police_station_id = police_staion_id
    police_station_vo.police_station_name = police_staion_name
    police_station_vo.lane_1 = lane_1
    police_station_vo.lane_2 = lane_2
    police_station_vo.district = district
    police_station_vo.state = state

    police_station_dao.update_ps(police_station_vo)

    return redirect("/admin/load_police_station_registration")










