# -*- coding: utf-8 -*-

# from datetime import datetime, date
#
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Sales Order Discount Amount"

    @api.model
    def default_get(self, fields):
        discount_amount = super(SaleOrder, self).default_get(fields)
        discount_amount ['discount_amount_sale'] = self.env['ir.config_parameter'].get_param('discount_amount_sale.discount_amount')
        return discount_amount

    discount_amount_sale = fields.Float(
        string="Discount Amount must be equal or less than",
        digits='Discount', help="Discount Amount must be less than the value",
        store=True, readonly=True)

    @api.onchange('order_line')
    def _onchange_order_line(self):
        for rec in self:
            for r in rec.order_line:
                if r.discount > rec.discount_amount_sale:
                    raise ValidationError(_('Discount Must be less than discount amount %s %%'% rec.discount_amount_sale))


    @api.constrains('discount_amount_sale')
    def check_discount(self):
        for rec in self:
            for amount in rec.order_line:
                if amount.discount > rec.discount_amount_sale:
                    raise ValidationError(_('Discount Must be less than discount amount %s %%'% rec.discount_amount_sale))



