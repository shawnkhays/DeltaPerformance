# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class prod_pack_dec(models.Model):
#     _name = 'prod_pack_dec.prod_pack_dec'
#     _description = 'prod_pack_dec.prod_pack_dec'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class prod_pack_dec(models.Model):
    _inherit = "product.packaging"
    # Adding decimal of 12, 3 to set the decimal precision to 3 to allow for better conversion.
    qty = fields.Float('Contained Quantity', digits = (12,3), help="Quantity of products contained in the packaging.")
