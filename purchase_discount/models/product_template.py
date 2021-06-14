# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    descuento = fields.Float(related="categ_id.category_discount")
    
    @api.depends("categ_id.parent_id.category_discount", "categ_id.category_discount", "seller_ids")
    def _compute_category_discount(self):
        for rec in self:
            categ_discount = 0
            for categ in rec.categ_id:
                descuento = categ.category_discount
                descuento_padre = categ.parent_id.category_discount
                if descuento:
                    categ_discount = descuento
                elif descuento_padre:
                    categ_discount = descuento_padre
            for line in seller_ids:
                self.env['product.supplierinfo'].write(
                    {
                        'discount': categ_discount
                    }
                )