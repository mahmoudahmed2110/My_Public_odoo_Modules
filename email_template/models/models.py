# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = 'email_template_for_sale_order'

    def send_email_template(self):
        self.env.ref("email_template.sale_email_template").send_mail(self.id, force_send=True)

    def return_string_from_backend_emailtemplate(self):
        return "Mahmoud-Reafat"



# class email_template(models.Model):
#     _name = 'email_template.email_template'
#     _description = 'email_template.email_template'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
