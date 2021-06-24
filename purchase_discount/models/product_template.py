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
            dis_cat = 0
            dis_par = 0
            discount = rec.categ_id.category_discount
            parent_discount = rec.categ_id.descuento_padre
            if parent_discount:
                dis_par = parent_discount
            if discount:
                dis_cat = discount
            rec.descuento = dis_cat
            rec.descuento_padre = dis_par