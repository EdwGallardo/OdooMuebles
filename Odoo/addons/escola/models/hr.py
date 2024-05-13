from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    is_teacher=fields.Boolean(string="Es professor")