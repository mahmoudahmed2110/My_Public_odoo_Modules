# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_amount = fields.Float(
        string="Discount (%)",
        digits='Discount', config_parameter='discount_amount_sale.discount_amount', readonly=False)



