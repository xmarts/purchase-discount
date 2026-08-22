# Copyright 2017 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# Copyright 2017-2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    discount = fields.Float(
        string="Discount (%)", digits="Discount", group_operator="avg"
    )

    def _select(self):
        return super()._select()

    def _group_by(self):
        return super()._group_by()

    def _get_discounted_price_unit_exp(self):
        pass
