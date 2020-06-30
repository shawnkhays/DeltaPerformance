# -*- coding: utf-8 -*-

from odoo import models, fields


class StockMove(models.Model):
    _inherit = "stock.move"

    def get_ordered_qty_bol_report(self):
        qty = self.product_uom_qty

        if self.sale_line_id:
            sale_order_line = self.sale_line_id
            if not sale_order_line.product_packaging:
                return sale_order_line.product_uom_qty
            else:
                for package in sale_order_line.product_id.packaging_ids:
                    if package.id == sale_order_line.product_packaging.id and package.product_uom_id.id == sale_order_line.product_uom.id:
                        return float(self.sale_line_id.product_uom_qty / package.qty)
                return qty

        return qty

    def get_shipped_qty_bol_report(self):
        qty = self.product_uom_qty
        if self.sale_line_id:
            sale_order_line = self.sale_line_id
            if not sale_order_line.product_packaging:
                return self.product_uom_qty
            else:
                for package in sale_order_line.product_id.packaging_ids:
                    if package.id == sale_order_line.product_packaging.id and package.product_uom_id.id == sale_order_line.product_uom.id:
                        return float(qty / package.qty)
                return qty

        return qty


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def get_ship_to_data(self):
        address = self.sale_id.partner_shipping_id._display_address()
        lines = address.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]

        string_without_empty_lines = ""
        for line in non_empty_lines:
            string_without_empty_lines += line + "\n"
        return string_without_empty_lines.replace('\n', '<br/>')

    def get_sold_to_data(self):
        address = self.sale_id.partner_id._display_address()
        lines = address.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]

        string_without_empty_lines = ""
        for line in non_empty_lines:
            string_without_empty_lines += line + "\n"
        return string_without_empty_lines.replace('\n', '<br/>')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    freight_charge = fields.Selection([('Collect', 'Collect'),
                                       ('Prepaid', 'Prepaid'),
                                       ('COD', 'COD')], string="Freight Charge",
                                      states={'done': [('readonly', True)], 'cancel': [('readonly', True)]}, copy=True)

    fob_remark = fields.Selection([('Warehouse', 'Warehouse'),
                                   ('Shipping Location', 'Shipping Location')], string="FOB Remark",
                                  states={'done': [('readonly', True)], 'cancel': [('readonly', True)]}, copy=True)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    customer_part_number = fields.Text('Customer Part #', copy=True)

    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['customer_part_number'] = self.customer_part_number
        return res


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    customer_part_number = fields.Text('Customer Part #', copy=True)


class ProductProduct(models.Model):
    _inherit = "product.product"

    freight_class = fields.Char('Freight Class')
    bol_shipping_description = fields.Text('BOL Shipping Description')


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def _prepare_invoice_values(self, order, name, amount, so_line):
        res = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(order, name, amount, so_line)
        if 'invoice_line_ids' in res:
            if res['invoice_line_ids']:
                res['invoice_line_ids'][0][2]['customer_part_number'] = so_line.customer_part_number
        return res
