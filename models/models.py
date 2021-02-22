# -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'school.teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "teacher record"
    _rec_name = 'name'

    name = fields.Char(string="Teacher Name", required=True)
    phone_number = fields.Char("Phone Number", size=11, )
    image = fields.Binary('Image', )
    # subject_id = fields.Many2one(comodel_name="school.subject", string="Subjects", required=False, )