# Copyright 2004-2009 Tiny SPRL (<http://tiny.be>).
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# Copyright 2015-2019 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def _add_supplier_to_product(self):
        return super()._add_supplier_to_product()


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    # adding discount to depends
    @api.depends("discount")
    def _compute_amount(self):
        return super()._compute_amount()

    def _convert_to_tax_base_line_dict(self):
        pass

    discount = fields.Float(string="Discount (%)", digits="Discount")

    _sql_constraints = [
        (
            "discount_limit",
            "CHECK (discount <= 100.0)",
            "Discount must be lower than 100%.",
        )
    ]

    def _get_discounted_price_unit(self):
        pass

    def _get_stock_move_price_unit(self):
        return super()._get_stock_move_price_unit()

    def _compute_price_unit_and_date_planned_and_name(self):
        return super()._compute_price_unit_and_date_planned_and_name()

    @api.model
    def _apply_value_from_seller(self, seller):
        pass

    def _prepare_account_move_line(self, move=False):
        return super()._prepare_account_move_line(move)

    @api.model
    def _prepare_purchase_order_line(
        self, product_id, product_qty, product_uom, company_id, supplier, po
    ):
        return super()._prepare_purchase_order_line(
            product_id, product_qty, product_uom, company_id, supplier, po
        )

    @api.model
    def _prepare_purchase_order_line_from_seller(self, seller):
        pass

    def write(self, vals):
        return super().write(vals)
