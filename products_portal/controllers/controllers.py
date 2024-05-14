# -*- coding: utf-8 -*-
# from odoo import http


# class ProductsPortal(http.Controller):
#     @http.route('/products_portal/products_portal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/products_portal/products_portal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('products_portal.listing', {
#             'root': '/products_portal/products_portal',
#             'objects': http.request.env['products_portal.products_portal'].search([]),
#         })

#     @http.route('/products_portal/products_portal/objects/<model("products_portal.products_portal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('products_portal.object', {
#             'object': obj
#         })
