# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID, api


def migrate(cr, version):
    # Re-run of the previous version's cleanup script: Odoo commits per
    # module (not once for the whole -u run), so if that script already
    # ran and committed on a prior attempt, it will not fire again on
    # retry even though the 16.0 views it was meant to delete are still
    # there -- and can still break an unrelated module that extends the
    # same inherited view chain. Bumping the version makes it pending again.
    env = api.Environment(cr, SUPERUSER_ID, {"active_test": False})
    imd = env["ir.model.data"].search([
        ("module", "=", "purchase_discount"),
        ("model", "=", "ir.ui.view"),
    ])
    views = env["ir.ui.view"].browse(imd.mapped("res_id")).exists()
    if views:
        views.with_context(_force_unlink=True).unlink()
