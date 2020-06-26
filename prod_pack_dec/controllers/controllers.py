# -*- coding: utf-8 -*-
# from odoo import http


# class ProdPackDec(http.Controller):
#     @http.route('/prod_pack_dec/prod_pack_dec/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prod_pack_dec/prod_pack_dec/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prod_pack_dec.listing', {
#             'root': '/prod_pack_dec/prod_pack_dec',
#             'objects': http.request.env['prod_pack_dec.prod_pack_dec'].search([]),
#         })

#     @http.route('/prod_pack_dec/prod_pack_dec/objects/<model("prod_pack_dec.prod_pack_dec"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prod_pack_dec.object', {
#             'object': obj
#         })
