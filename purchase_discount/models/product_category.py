# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class ProductCategory(models.Model):
    _inherit = "product.category"

    category_discount =  fields.Float(string="Category Discount (%)")

    descuento_padre = fields.Float(compute="_compute_category_discount")
    
    @api.depends("categ_id.parent_id.category_discount",)
    def _compute_category_discount(self):
        for rec in self:
            categ_discount = 0
            for categ in rec.categ_id:
                descuento = categ.parent_id.category_discount
                if descuento:
                    categ_discount = descuento_padre
            rec.descuento_padre = categ_discount