# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FurnitureMangement(models.Model):
    _name = 'furniture.management'
    _description = 'furniture'
    _order = "name, start_date desc"
    _recname = "name"

    name = fields.Char(string="Name", default="Set Name for furniture", translate=True, trim=False, readonly=False, required=True) #trim fot first space
    value = fields.Integer(string="Value")
    active = fields.Boolean(string="Active")
    colour = fields.Selection([
        ('white', 'White'),
        ('black', 'Black'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('Blue', 'Blue'),
        ('move', 'Move'),
        ('other', 'Other'),
    ], string="Colour", default='white')
    area = fields.Float(string="Area")
    price = fields.Monetary("Price", currency_field="currency_id")
    reference =  fields.Reference(selection=[("res.company","Company"),
                                             ("res.partner","Partner"),
                                             ("res.currency","Currency"),
                                             ] , string="Reference")
    currency_id = fields.Many2one('res.currency', string="Currency")
    note = fields.Text(string="Note")
    descr = fields.Html("Description")
    image = fields.Image(string="Image")
    data_files = fields.Binary(string="Data_files", store=True)
    start_date = fields.Datetime(string="Start_Date", default=lambda self: fields.Datetime.now())
    finished_date = fields.Date(string="Finished_Date")
    worker = fields.Many2many("res.partner", string="Worker")
    department = fields.Many2one("furniture.departments", ondelete="cascade", string="Department")

