# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrPayslibInherit(models.Model):
    _inherit = 'hr.payslip'
    _description = 'Inherit Hr Payslib'

    penalities_ids = fields.One2many(related="employee_id.penalities_ids", string="Penalities")
    # penalty_this_m = fields.Flaut(string="Total Penalty this Month", compute="_compute_penalty_this_month")
    #
    # @api.depends('date_from', 'date_to')
    # def _compute_penalty_this_month(self):
    #     for rec in self:
    #         for pen in rec.penalities_ids:
    #             if
