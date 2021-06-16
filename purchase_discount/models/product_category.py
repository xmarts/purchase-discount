# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class ProductCategory(models.Model):
    _inherit = "product.category"

    category_discount =  fields.Float(string="Category Discount (%)")

    descuento_padre = fields.Float(compute="_compute_category_discount")
    
    @api.depends("parent_id.category_discount",)
    def _compute_category_discount(self):
        for rec in self:
            categ_discount = 0
            descuento = rec.parent_id.category_discount
            if descuento:
                categ_discount = descuento
        rec.descuento_padre = categ_discount

    @api.depends("category_discount")
    def _env_category_discount(self):
        for rec in self:
            dicount = rec.category_discount
            if discount:
                self.env["product.template"].search([('categ_id', '=', self.id)]).write("descuento":discount)
