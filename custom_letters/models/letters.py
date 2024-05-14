# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LettersRequests(models.Model):
    _name = 'letters.requests'
    _description = 'letters.requests'

    name = fields.Char(string="Letter Subject")
    image = fields.Image(string="Image")
    request_owner_id = fields.Many2one("res.users", string="Request Owner")
    category = fields.Selection([
        ('friendship', 'FriendShip'),
        ('familial', 'Family'),
        ('congratulate', 'Congratulation'),
    ], string="Category", default='familial')

    state = fields.Selection([
        ('to submit', 'TO SUBMIT'),
        ('submitted', 'SUBMITTED'),
        ('approved', 'APPROVED'),
        ('refused', 'REFUSED'),
        ('cancel', 'CANCELLED')
    ], string='Status', readonly=True, default='to submit')

    date_confirmed = fields.Datetime(string="Date Confirmed", default=lambda self: fields.Datetime.now(), readonly=True)
    description = fields.Html(string="Description")

    def button_submitted(self):
        self.state = 'submitted'
        return {}

    def button_approved(self):
        self.state = 'approved'
        return {}

    def button_to_refuse(self):
        self.state = 'refused'
        return {}
    def button_cancel(self):
        self.state = 'cancel'
        return {}
    def button_return_to_submit(self):
        self.state = 'to submit'
        return {}
