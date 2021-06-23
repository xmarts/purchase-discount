# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    descuento = fields.Float(string="Category Discount (%)",
        compute="_compute_category_discount")
    
    descuento_padre = fields.Float(string="Category Discount (%)",
        compute="_compute_category_discount")

    @api.depends("categ_id.category_discount","categ_id.descuento_padre")
    def _compute_category_discount(self):
        for rec in self:
            discount = rec.categ_id.category_discount
            parent_discount = rec.categ_id.descuento_padre
            if parent_discount:
                rec.descuento_padre = parent_discount
            if discount:
                rec.descuento = discount