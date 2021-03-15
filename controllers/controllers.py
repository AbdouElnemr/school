from odoo import http
from odoo.http import request
import json
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleInherit(WebsiteSale):
    @http.route([
        '''/shop''',
        '''/shop/page/<int:page>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>''',
        '''/shop/category/<model("product.public.category", "[('website_id', 'in', (False, current_website_id))]"):category>/page/<int:page>'''
    ], type='http', auth="public", website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        print("inherited odoo mates")
        res = super(WebsiteSaleInherit, self).shop(page=0, category=None, search='', ppg=False, **post)


class Hospital(http.Controller):
    # @http.route('/school/teachers/', website=True, auth='public')
    # def index(self, **kw):
    #     patients = request.env['school.teacher'].sudo().search([])
    #     return request.render("om_school.patients_page", {
    #         'patient': patients,
    #     })

    @http.route('/web/session/authenticate', type="json", auth='none')
    def authenticate(self, db, login, password, base_location=None):
        request.session.authinticate(db, login, password)
        return request.env['ir.http'].session_info()

    @http.route('/om_school/appointments', type="json", auth='none')
    def appointment_banner(self):
        return {
            'html': """
                    <div>
                        </br>
                        </br>
                            <center><h1><font color="red"> Test Banner route </font></h1></center>
                        </br>
                        </br>
                    </div>
                    """
        }
    #

    @http.route('/update_teacher', type="json", auth='user', )
    def update_teacher(self, **rec):
        if request.jsonrequest:
            if rec['id']:
                data = {}
                patient = request.env['school.patient'].sudo().search([('id', '=', rec['id'])])
                if patient:
                    patient.sudo().write(rec)
                    data = {
                        'name': patient.patient_name,
                        'age': patient.patient_age,
                        'doctor': patient.doctor_id.doctor_name
                    }
                args = {
                    'message': 'success',
                    'success': 'True',
                    'response': data,
                }
        return args

    @http.route('/web/session/destroy', type='json', auth="user")
    def destroy(self):
        request.session.logout()

    @http.route('/create_teacher', type="json", auth='public', )
    def create_patient(self, **rec):
        if request.jsonrequest:
            if rec['name']:
                vals = {
                    'name': rec['name'],
                    'phone_number': rec['phone_number'],
                    'subject_id': rec['subject_id'],
                }
                new_teacher = request.env['school.teacher'].sudo().create(vals)
                args = {
                    'meaasge': 'success',
                    'success': 'True',
                    'data':
                        {
                            'id': new_teacher.id,
                            'name': new_teacher.name
                         },
                }
        return args

    @http.route('/get_teachers', type="json", auth='public', csrf=False )
    def get_all_teachers(self):
        # get all teachers
        teachers_rec = request.env['school.teacher'].search([])
        teachers = []
        for rec in teachers_rec:
            print("rec.image", type(rec.image))
            vals = {
                'id': rec.id,
                'name': rec.name,
                'subject': rec.subject_id.name,
                'phone': rec.phone_number,
                'image': rec.image,
            }
            teachers.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': teachers,
        }
        return data

    @http.route('/get_students', type="json", auth='public',csrf=False )
    def get_all_students(self):
        # get all patients
        students_rec = request.env['school.student'].search([])
        students = []
        for rec in students_rec:
            tt = []
            for t in rec.teacher_ids:
                tt.append({t.name})
            vals = {
                'id': rec.id,
                'birth_date': rec.birth_date,
                'name': rec.name,
                'class_id': rec.class_id.name,
                'teachers': tt
            }
            students.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': students,
        }
        return data

