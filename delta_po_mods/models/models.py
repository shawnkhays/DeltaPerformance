# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class delta_po_mods(models.Model):
#     _name = 'delta_po_mods.delta_po_mods'
#     _description = 'delta_po_mods.delta_po_mods'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
