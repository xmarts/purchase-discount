# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    descuento = fields.Float(related="categ_id.category_discount")
    descuento_padre = fields.Float(related="categ_id.descuento_padre")

    @api.depends("categ_id.parent_id.category_discount", "categ_id.category_discount", "seller_ids","seller_ids.price")
    def _compute_category_discount(self):
        for rec in self:
            discount = rec.descuento
            parent_discount = rec.descuento_padre
            if descuento:
                categ_discount = discount
            elif descuento_padre:
                categ_discount = parent_discount
        for line in seller_ids:
            self.env['product.supplierinfo'].write(
                {
                    'discount': categ_discount
                }
            )