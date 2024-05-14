# -*- coding: utf-8 -*-
# from odoo import http


# class EmailTemplate(http.Controller):
#     @http.route('/email_template/email_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/email_template/email_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('email_template.listing', {
#             'root': '/email_template/email_template',
#             'objects': http.request.env['email_template.email_template'].search([]),
#         })

#     @http.route('/email_template/email_template/objects/<model("email_template.email_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('email_template.object', {
#             'object': obj
#         })
