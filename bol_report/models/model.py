# -*- coding: utf-8 -*-

from odoo import models, fields


class StockPicking(models.Model):
    _inherit = "stock.picking"

    freight_charge = fields.Selection([('Collect', 'Collect'),
                                       ('Prepaid', 'Prepaid'),
                                       ('COD', 'COD')], string="Freight Charge",
                                      states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})

    fob_remark = fields.Selection([('Warehouse', 'Warehouse'),
                                   ('Shipping Location', 'Shipping Location')], string="FOB Remark",
                                  states={'done': [('readonly', True)], 'cancel': [('readonly', True)]})

    def get_ship_to_data(self):
        address = self.sale_id.partner_shipping_id._display_address()
        return address.replace('\n', '<br/>')

    def get_sold_to_data(self):
        address = self.sale_id.partner_id._display_address()
        return address.replace('\n', '<br/>')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_part_number = fields.Text('Customer Part #', copy=True)

    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        res['customer_part_number'] = self.customer_part_number
        return res


class AccountMove(models.Model):
    _inherit = "account.move"

    customer_part_number = fields.Text('Customer Part #', copy=True)


class ProductProduct(models.Model):
    _inherit = "product.product"

    freight_class = fields.Char('Freight Class')
    bol_shipping_description = fields.Text('BOL Shipping Description')


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        res = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(order, name, amount, so_line)
        res['customer_part_number'] = order.customer_part_number
        return res