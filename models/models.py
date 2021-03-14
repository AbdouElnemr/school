# -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'school.teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "teacher record"

    name = fields.Char(string="Teacher Name", required=True)
    phone_number = fields.Char("Phone Number", size=11, )
    image = fields.Binary('Image', )
    subject_id = fields.Many2one("school.subject", string="Subject", required=False, )
    #
    # def _get_teacher_subjects(self):
    #     for rec in self:
    #         subjects = rec.env['school.subject'].search([('teacher_id', '=', self.id)])
    #         for subject in subjects:
    #             self.subject_id = subject.teacher_ids.name