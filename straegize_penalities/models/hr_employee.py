# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    _description = 'Inherit Hr Employee'

    penalities_ids = fields.One2many("penaltiesemp.penaleties", "employee_id", string="Penalities")