from base import db
from base.com.Vo.admin_vo import AdminVo

class AdminDao:

    def insert_admin(self,admin_vo):
        db.session.add(admin_vo)
        db.session.commit()

    def view_admin(self):
        admin_list = AdminVo.query.all()
        return admin_list

    def delete_admin(self,admin_vo):
        admin_list = AdminVo.query.get(admin_vo)
        db.session.delete(admin_list)
        db.session.commit()

    def edit_admin(self,admin_vo):
        return AdminVo.query.get(admin_vo)

    def update_admin(self,admin_vo):
        admin = AdminVo.query.get(admin_vo.admin_id)
        admin.first_name = admin_vo.first_name
        admin.middle_name = admin_vo.middle_name
        admin.last_name = admin_vo.last_name
        admin.user_name = admin_vo.user_name
        admin.password = admin_vo.password
        admin.date_of_birth = admin_vo.date_of_birth
        db.session.commit()