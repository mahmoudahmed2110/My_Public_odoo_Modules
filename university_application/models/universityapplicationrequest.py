# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime, timedelta

class UniversityApplicationRequest(models.Model):
    _name = "university.request"
    _description = "University Application Request"

    name = fields.Char(string="Student Name", required=True)
    student_address = fields.Text(string="Student Address")
    national_id = fields.Char(string="Student National ID", required=True, size=14)
    image = fields.Image(string="Image")
    birthdate = fields.Date(string="Birth Date", default=date.today())
    age = fields.Integer(string="Age", compute="_compute_age", readonly=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','Female')], default="male", string="Gender")
    mobile1 = fields.Char(string="Student Mobile", size=13, required=True)
    mobile2 = fields.Char(string="Student Mobile-2", size=13)
    email = fields.Char(string="Student Email")

    student_length = fields.Float(string="Student Length")
    student_wieght = fields.Float(string="Student Wieght")
    secondary_certificate = fields.Image(string="Secondary Certificate")
    results_total_degree = fields.Float(string="Secondary Results Total")
    results_total_percentage = fields.Float(string="Secondary Results Percentage")
    studentrelatives_ids = fields.Many2many("university.studentrelatives", string="Student Relatives")

    faculty_ids = fields.Many2many("university.faculty", string="Faculties")
    skills = fields.Text(string="Student Skills")
    Talents = fields.Text(string="Student Talents")


    @api.depends('birthdate')
    def _compute_age(self):
        for rec in self:
            currentyear = date.today()
            if rec.birthdate:
                rec.age = currentyear.year - rec.birthdate.year
            else:
                rec.age = 1
