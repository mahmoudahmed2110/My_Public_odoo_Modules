# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError


class PenaltiesEmp(models.Model):
    _name = 'penaltiesemp.penaleties'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'penaleties description'

    name = fields.Char(string="Summary Of  Penalty", required=True, track_visibility="always")
    penalty_date_declaration = fields.Date(string="Date Of Declaration", required=True, track_visibility="always")
    penalty_date_apply = fields.Date(string="Date Of Application", required=True, track_visibility="always")
    employee_id = fields.Many2one("hr.employee", string="Employee Name")
    company_id = fields.Many2one(
        'res.company', string='Company', copy=False, required=True,
        compute='_compute_company_id', store=True, readonly=False,
        default=lambda self: self.env.company,
    )
    payslib_id = fields.Many2one("hr.payslip", string="Employee")
    penalty_type = fields.Selection([
        ('amount','Amount'),
        ('percentage','Percentage'),
    ], string="Penalty Type", track_visibility="always")
    penalty_value = fields.Float(string="Penalty Value", track_visibility="always")
    penalty_details = fields.Text(string="Details Of Penalty", track_visibility="always")

    @api.depends('employee_id')
    def _compute_company_id(self):
        for slip in self.filtered(lambda p: p.employee_id):
            slip.company_id = slip.employee_id.company_id

