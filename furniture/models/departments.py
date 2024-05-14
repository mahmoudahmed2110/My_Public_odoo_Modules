# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FurnitureDepartments(models.Model):
    _name = 'furniture.departments'
    _description = 'departments'

    name = fields.Char(string="Name")
    image = fields.Image(string="Image")
    size = fields.Char(string="Size")
    mobile = fields.Char(string="Department_Mobile", size=13)
    notes = fields.Html(string="Notes")
