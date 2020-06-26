# -*- coding: utf-8 -*-
# from odoo import http


# class DeltaPoMods(http.Controller):
#     @http.route('/delta_po_mods/delta_po_mods/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delta_po_mods/delta_po_mods/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delta_po_mods.listing', {
#             'root': '/delta_po_mods/delta_po_mods',
#             'objects': http.request.env['delta_po_mods.delta_po_mods'].search([]),
#         })

#     @http.route('/delta_po_mods/delta_po_mods/objects/<model("delta_po_mods.delta_po_mods"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delta_po_mods.object', {
#             'object': obj
#         })
