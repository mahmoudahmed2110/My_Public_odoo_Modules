# -*- coding: utf-8 -*-

from odoo import models, fields, tools, api
from datetime import date, datetime, timedelta
from odoo.addons import decimal_precision as dp
from dateutil import relativedelta

class YDSPurchaseRequest(models.Model):
    _name = "purchase.request"
    _description = "Purchase Request"

    name = fields.Char('Purchase Reference', required=True, index=True, copy=False, default='New')
    state = fields.Selection([
        ('draft', 'RFQ'),
        ('confirm', 'Confirmed')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    account_analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account')
    create_date = fields.Date(string="Create Date", readonly=True, default=date.today())
    requested_user = fields.Many2one('res.users', string='Purchase Requested by', default=lambda self: self.env.user)
    requested_on_date = fields.Date(sring="Date of Request", default=date.today())

    order_line = fields.One2many('purchase.order.line', 'purchase_request_id', string="Order Lines")
    partner_id = fields.Many2one('res.partner', related='partner_id', string='Partner', readonly=True, store=True)
    product_id = fields.Many2one('product.product', related='order_line.product_id', string='Product', readonly=False)
    product_qty = fields.Float(string='Quantity', digits=dp.get_precision('Product Unit of Measure'))
    product_uom = fields.Many2one('uom.uom', string='Product Unit of Measure')






    class PurchaseOrderLine(models.Model):
        _inherit = 'purchase.order.line'

        purchase_request_id = fields.Many2one('purchase.request', 'Purchase Request')
        partner_id = fields.Many2one('res.partner', string='Vendor')

    @api.multi
    def button_confirm(self):
        for order in self:
            if order.state not in ['draft']:
                continue
            else:
                order.write({'state': 'confirm'})


    @api.multi
    def button_cancel(self):
        for order in self:
            if order.state not in ['confirm']:
                continue
            else:
                order.write({'state': 'draft'})
