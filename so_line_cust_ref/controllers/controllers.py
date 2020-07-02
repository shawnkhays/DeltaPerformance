# -*- coding: utf-8 -*-
# from odoo import http


# class SoLineCustRef(http.Controller):
#     @http.route('/so_line_cust_ref/so_line_cust_ref/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/so_line_cust_ref/so_line_cust_ref/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('so_line_cust_ref.listing', {
#             'root': '/so_line_cust_ref/so_line_cust_ref',
#             'objects': http.request.env['so_line_cust_ref.so_line_cust_ref'].search([]),
#         })

#     @http.route('/so_line_cust_ref/so_line_cust_ref/objects/<model("so_line_cust_ref.so_line_cust_ref"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('so_line_cust_ref.object', {
#             'object': obj
#         })
