# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _name = 'school.task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "task record"

    name = fields.Char(string="Name", required=False, )
    age = fields.Integer(string="Age", required=False, )
    status = fields.Char(string="Status", required=False, default=" not uploaded")
    