# -*- coding: utf-8 -*-

from odoo import models, fields, tools, api
# from odoo.exceptions import ValidationError
# from odoo.http import request
# from odoo.modules import get_module_resource
# from odoo.osv import expression

from datetime import date, datetime, timedelta
from dateutil import relativedelta

class LawyersManagment(models.Model):
    _name = "lawyers"
    _description = "Lawyers Managment"
#    _rec_name ="new_field"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", compute='compute_age')
    date = fields.Date(sring="Date of Birth")
    notes = fields.Text(string="NOtes")

    @api.depends('date')
    def compute_age(self):
        for rec in self:
            currentyear = date.today()
            if rec.date:
                rec.age = currentyear.year - rec.date.year
            else:
                rec.age = 3

    #10-ORM-Models-Fields-

    # _sql_constraints = [
    #     ('age_check', 'check (age >= 21)', 'Can not be less than 21 Years'),
    # ]
    # _sql_constraints = [
    #     ('check_name_field', 'unique (name)', 'Name can not be duplicated'),
    # ]
    #09-01_sql_constraints
    #check unique values _sql_constraints = [
    #     ('', 'unique ()', '')
    # ]
    #check creiteria like date currency _sql_constraints = [
    #     ('', 'check ()', '')
    # ]
    #08Reference fields&Float fields

    # reference =  fields.Reference(selection=[('res.company','Company'),
    #                                          ('res.currency','Currency'),
    #                                          ] , string='Reference')
    # weight = fields.Float(string='Weight', digits='Payment Terms', required=True)
    #
    #07with  res.users
    #07lawyer_id = fields.Many2one('res.users', string='Lawyers')
    # price = fields.Monetary(currency_field='currency_id', string="price")
    # currency_id = fields.Many2one('res.currency', string="Currency", related='company_id.currency_id')
    # company_id = fields.Many2one('res.company', string='Company')
    # #07company_id = fields.Many2one('res.company', string='Company', related='lawyer_id.company_id')
    #06customers_id = fields.Many2one("customers", string="customers")
    #06customers_ids = fields.Many2many("customers", string="Customer Many")
    #06customer_id = fields.One2many("customers", "lawyer_id", string="Customer Many")

    #05age = fields.Integer(string="Age", compute="_compute_age")
    #05date = fields.Date(string="Date Field", default=date.today())
    #05time = fields.Datetime(string="Datetime Field")

    # 05@api.depends('date')
    # 05def _compute_age(self):
    #     for rec in self:
    #         currentyear = date.today()
    #         if rec.date:
    #             rec.age = currentyear.year - rec.date.year
    #         else:
    #             rec.age = 1
#04Basic fields
    # new_field = fields.Char(string="New field")
    # field02 = fields.Text(string="Text field")
    # field03 = fields.Selection([
    #     ('male','Male'),
    #     ('female','Female')], string="Selection_field")
    # field04 = fields.Boolean(string="Boolean field")
    # field05 = fields.Html(string="Html field")
    # field06 = fields.Image(string="Image field")
    # field07 = fields.Binary(string="Binary field")
    # field08 = fields.Integer(string="Integer field")
    # field09 = fields.Float(string="Float field")


