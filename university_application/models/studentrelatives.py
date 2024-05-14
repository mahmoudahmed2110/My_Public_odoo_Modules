# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityStudentrelatives(models.Model):
    _name = "university.studentrelatives"
    _description = "Students Relatives"

    name = fields.Char(string="Student Relative Name", required=True)
    image = fields.Image(string="Image")
    age = fields.Integer(string="Age")
    mobile = fields.Char(string="Relative Mobile", size=13)
    notes = fields.Text(string="Relative notes")
    university_request_id = fields.Many2many("university.request", string="Student Name", readonly=True)
