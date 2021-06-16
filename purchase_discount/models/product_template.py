# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    descuento = fields.Float()
    descuento_padre = fields.Float(related="categ_id.descuento_padre")
