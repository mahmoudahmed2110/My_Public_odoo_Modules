# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityFaculty(models.Model):
    _name = "university.faculty"
    _description = "University faculty"

    name = fields.Char(string="Faculty Name")
    image = fields.Image(string="Image")
    address = fields.Char(string="Faculty Address")
    mobile = fields.Char(string="Faculty Mobile", size=13)
    mobile2 = fields.Char(string="Faculty Mobile-2", size=13)
    email = fields.Char(string="Faculty Email")
    location = fields.Char(string="Faculty GPS Location")
    notes = fields.Html(string="Faculty Notes")

    request_ids = fields.Many2many("university.request", string="Student Requests", readonly=True)


