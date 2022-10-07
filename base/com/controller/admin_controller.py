from flask import *
from  base import app
import re
from base.com.Dao.admin_dao import AdminDao
from base.com.Vo.admin_vo import AdminVo

app.secret_key = "asdazxzzdlqwihihjbejkTdsbjfbjsaJSTqqq1228hb778"

@app.route("/")
def load_loginpage():
    return render_template("/admin/admin_login.html")

@app.route("/admin/login_page",methods=["POST"])
def admin_login():

    user_name = request.form.get("un")
    password = request.form.get("pas")

    admin_dao = AdminDao()

    alist = admin_dao.view_admin()
    username_list = [i.as_dict()['user_name'] for i in alist]
    password_list = [i.as_dict()['password'] for i in alist]
    admin_id_list = [i.as_dict()['admin_id'] for i in alist]

    if user_name not in username_list:
        flash("Username does not exist!!")
        return render_template("/admin/admin_login.html")

    index = username_list.index(user_name)
    admin_id = admin_id_list[index]
    print(admin_id,index)
    session['admin_id'] = admin_id
    pas = password_list[index]

    if pas==password:
        return render_template("/admin/admin_homepage.html")

    else:
        flash("Passowrd Incorrect!!")
        return render_template("/admin/admin_login.html")

@app.route("/admin/load_registration_page")
def load_registration_page():
    return render_template("/admin/admin_register.html")

@app.route("/admin/registration_page",methods=["POST"])
def admin_registration():

    first_name = request.form.get("fn")
    middle_name = request.form.get("mn")
    last_name = request.form.get("ln")
    user_name = request.form.get("un")
    password = request.form.get("pas")
    date_of_birth = request.form.get("dob")

    admin_vo = AdminVo()
    admin_dao = AdminDao()

    alist = admin_dao.view_admin()
    username_list = [i.as_dict()['user_name'] for i in alist]

    if user_name in username_list:
        flash("Username already exist!!")
        return render_template("/admin/admin_register.html")

    special_characters = """!"'@"""+"""+*|\?{}[]~`:$%^&*()-+?_=,<>/#"""

    if (re.search('[a-z]',password) and re.search('[A-Z]',password) and
        re.search(r'\d', password) and len(password)>=8 and any(c in special_characters for c in password) ):

        admin_vo.first_name = first_name
        admin_vo.middle_name = middle_name
        admin_vo.last_name = last_name
        admin_vo.user_name = user_name
        admin_vo.password = password
        admin_vo.date_of_birth = date_of_birth

        admin_dao.insert_admin(admin_vo)

        return redirect("/")

    else:
        flash("There must be:")
        flash("8 characters")
        flash("1 lowercase")
        flash("1 uppercase")
        flash("1 numeric-value")
        flash("1 special-character")
        return render_template("/admin/admin_register.html")


@app.route("/admin/admin_load_homepage")
def load_homepage():
    return render_template("/admin/admin_homepage.html")

@app.route("/admin/admin_view")
def admin_view():

    admin_dao = AdminDao()
    alist = admin_dao.view_admin()

    return render_template("/admin/admin_view.html",alist=alist)

@app.route("/admin/admin_delete")
def admin_delete():

    admin_vo = AdminVo()
    admin_dao = AdminDao()

    admin_id = session['admin_id']

    admin_vo.admin_id = admin_id
    admin_dao.delete_admin(admin_vo.admin_id)

    return redirect("/admin/admin_view")

@app.route("/admin/admin_edit")
def admin_edit():

    admin_vo = AdminVo()
    admin_dao = AdminDao()

    admin_id = session['admin_id']

    admin_vo.admin_id = admin_id
    id_list = admin_dao.edit_admin(admin_vo.admin_id)

    return render_template("/admin/admin_update.html",id_list=id_list)

@app.route("/admin/admin_update",methods=["POST"])
def admin_update():

    first_name = request.form.get("fn")
    middle_name = request.form.get("mn")
    last_name = request.form.get("ln")
    user_name = request.form.get("un")
    password = request.form.get("pas")
    date_of_birth = request.form.get("dob")

    admin_vo = AdminVo()
    admin_dao = AdminDao()

    alist = admin_dao.view_admin()
    admin_id = session['admin_id']
    username_list = [i.as_dict()['user_name'] for i in alist]
    id_list = [i.as_dict()['admin_id'] for i in alist]
    index = id_list.index(admin_id)

    if username_list[index]!=user_name and user_name in username_list:
        flash("Username already exist!!")
        return redirect("/admin/admin_edit")

    admin_vo.admin_id = session['admin_id']
    admin_vo.first_name = first_name
    admin_vo.middle_name = middle_name
    admin_vo.last_name = last_name
    admin_vo.user_name = user_name
    admin_vo.password = password
    admin_vo.date_of_birth = date_of_birth

    admin_dao.update_admin(admin_vo)

    return redirect("/admin/admin_view")











