# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductCategory(models.Model):
    _inherit = "product.category"

    category_discount = fields.Float(string="Category Discount (%)")
    descuento_padre = fields.Float(related="parent_id.category_discount")
