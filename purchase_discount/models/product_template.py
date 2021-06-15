# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    descuento = fields.Float(related="categ_id.category_discount")
    descuento_padre = fields.Float(related="categ_id.descuento_padre")

    @api.depends("descuento_padre", "descuento", "seller_ids","seller_ids.price")
    def _compute_category_discount(self):
        for rec in self:
            discount = rec.descuento
            parent_discount = rec.descuento_padre
            if discount:
                categ_discount = discount
            elif parent_discount:
                categ_discount = parent_discount
        for line in seller_ids:
            self.env['product.supplierinfo'].write(
                {
                    'discount': categ_discount
                }
            )