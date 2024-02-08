# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    descuento = fields.Float(
        string="Category Discount (%)",
        related="categ_id.category_discount"
    )

    descuento_padre = fields.Float(
        string="Category Discount (%)",
        related="categ_id.descuento_padre"
    )
