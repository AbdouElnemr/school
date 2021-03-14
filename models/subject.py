# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Subject(models.Model):
    _name = 'school.subject'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "subject record"

    sequence = fields.Integer(string="Sequence", )
    name = fields.Char(string="Subject Name", )
    # teacher_ids = fields.Many2one("school.teacher", string="Teacher", )

    # @api.onchange("arabic")
    # def on_ar_change(self):
    #     self.arabic = 0.0

    #
    # @api.multi
    # def create_student_report(self):
    #     data = {'model': 'payroll_salary.wizard', 'form': self.read()[0]}
    #     students = self.env['school.student'].search([])
    #     for rec in self:
    #         if rec.teacher_ids:
    #             for student in students:
    #                 if student.teacher_ids.id in rec.teacher_ids:
    #                     print(student.name)

    # return self.env.ref('school.student_report_print').report_action(self, data)
