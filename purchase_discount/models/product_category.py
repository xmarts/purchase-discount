# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
    
class ProductCategory(models.Model):
    _inherit = "product.category"

    category_discount = fields.Float(
        string="Category Discount (%)")

    descuento_padre = fields.Float(string="Parent Category Discount (%)",
        compute="_compute_category_discount")

    @api.depends("parent_id.category_discount")
    def _compute_category_discount(self):
        for rec in self:    
            if rec.parent_id.category_discount:
                rec.descuento_padre = rec.parent_id.category_discount