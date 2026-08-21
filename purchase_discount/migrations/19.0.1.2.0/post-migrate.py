# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    # Delete views left over from the 16.0 install now that this module's
    # manifest no longer loads any views/*.xml file. _force_unlink mirrors
    # module uninstall: it cascades through inherit_children_ids even when
    # the child view belongs to a different module, avoiding FK errors.
    env = api.Environment(cr, SUPERUSER_ID, {})
    imd = env["ir.model.data"].search([
        ("module", "=", "purchase_discount"),
        ("model", "=", "ir.ui.view"),
    ])
    views = env["ir.ui.view"].browse(imd.mapped("res_id")).exists()
    if views:
        views.with_context(_force_unlink=True).unlink()
