# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    descuento = fields.Float(string="Category Discount (%)",
        compute="_compute_category_discount")
    
    descuento_padre = fields.Float(string="Category Discount (%)",
        compute="_compute_category_discount")

    @api.depends("categ_id.category_dicount")
    def _compute_category_discount(self):
        for rec in self:
            if rec.categ_id.category_discount:
                rec.descuento_padre = rec.parent_id.descuento_padre
            if rec.    
                rec.descuento = rec.categ_id.category_discount