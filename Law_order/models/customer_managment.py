# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, datetime, timedelta
from dateutil import relativedelta

class CustomersManagment(models.Model):
    _name = "customers"
    _description = "Customer Managment"
    _inherits = {
        'lawyers':'lawyer_id',
    }
#    _rec_name ="new_field"

    name = fields.Char(string="Name", related="lawyer_id.name", readonly=False)
    age = fields.Integer(string="Age")

    my_text = fields.Text(string="My Text")
    active = fields.Boolean(string="Active")
    another_boolean = fields.Boolean(string="Another Boolean")

    state = fields.Selection([])

    #15oRM METHODS

    def print_record(self):
        domain = [('age','>=',30)]
        print(self.env['customers'].search(domain))
        for rec in filtered_customer:
            rec.name = "Old_users"

    #11environment&related_fields
    # def create_record(self):
    #     for rec in self:
    #         rec.my_text = self.env['lawyers'].search([('age','>=',30)])
    lawyer_id = fields.Many2one('lawyers', string='Lawyers')

    # currency_id = fields.Many2one('res.currency', string="Currency", related='company_id.currency_id')
    # company_id = fields.Many2one('res.company', string='Company')

    #10modlesfieldsApiandrecord set&11environment and related fields
    # def create_record(self):
    #     for rec in self:
    #         rec.my_text = self.env['res.users'].search([('age','>=',30)])
    # def create_record(self):
    #     for rec in self:
    #         rec.my_text = self.env['lawyers'].search([('age','>=',30)])

    # def compute_age(self):
    #     for rec in self:
    #         print(self.env.user.name)

    #09-02_api_constraints
    # @api.constrains('age')
    # def check_age(self):
    #     if self.age < 21:
    #         raise ValidationError(_('Age Can be less than required 21'))

    # lawyer_id = fields.Many2one("lawyers", string="lawyers")


    # age = fields.Integer(string="Age", compute="_compute_age")
    # date = fields.Date(string="Date Field", default=date.today())
    # time = fields.Datetime(string="Datetime Field")

    # @api.depends('date')
    # def _compute_age(self):
    #     for rec in self:
    #         currentyear = date.today()
    #         if rec.date:
    #             rec.age = currentyear.year - rec.date.year
    #         else:
    #             rec.age = 1

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


