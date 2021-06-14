# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _

class ProductCategory(models.Model):
    _inherit = "product.category"

    category_discount =  fields.Float(string="Category Discount (%)", default=0)

