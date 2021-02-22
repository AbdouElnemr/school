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
    @http.route('/school/teachers/', website=True, auth='public')
    def index(self, **kw):
        patients = request.env['school.teacher'].sudo().search([])
        return request.render("om_school.patients_page", {
            'patient': patients,
        })

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

    @http.route('/create_patient', type="json", auth='user', )
    def create_patient(self, **rec):
        if request.jsonrequest:
            if rec['name']:
                vals = {
                    'patient_name': rec['name'],
                    'patient_age': rec['age'],
                    'doctor_id': rec['doctor'],
                }
                new_patient = request.env['school.patient'].sudo().create(vals)
                args = {
                    'meaasge': 'success',
                    'success': 'True',
                    'id': new_patient.id,
                }
        return args

    @http.route('/update_patient', type="json", auth='user', )
    def update_patient(self, **rec):
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

    @http.route('/get_teachers', type="json", auth='public', csrf=False )
    def get_all_teachers(self):
        # get all patients
        patients_rec = request.env['school.teacher'].search([])
        teachers = []
        for rec in patients_rec:
            vals = {
                'id': rec.id,
                # 'patient_id': rec.name_seq,
                'name': rec.name,
                # 'age': rec.patient_age,
                # 'doctor': rec.doctor_id.doctor_name
            }
            teachers.append(vals)
        data = {
            'status': "200",
            'message': "success",
            'response': teachers,
        }
        return data


    @http.route('/get_students', type="json", auth='user', )
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

    # @http.route('/om_school/om_school/objects/<model("om_school.om_school"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('om_school.object', {
    #         'object': obj
    #     })
