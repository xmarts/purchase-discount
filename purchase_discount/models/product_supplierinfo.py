# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# Copyright 2014-2019 Tecnativa - Pedro M. Baeza
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ProductSupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    discount = fields.Float(string='Discount (%)', digits='Discount', store=True, readonly=False)

    @api.depends("partner_id")
    def _compute_discount(self):
        pass

    @api.model
    def _get_po_to_supplierinfo_synced_fields(self):
        pass

    @api.model_create_multi
    def create(self, vals_list):
        return super().create(vals_list)
