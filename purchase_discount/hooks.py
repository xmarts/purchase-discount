from odoo import api, SUPERUSER_ID

def pre_init_hook(cr):
    """Ejecutar antes de la instalación del módulo"""
    pass

def post_init_hook(cr, registry):
    """Ejecutar después de la instalación del módulo"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['migration.fixes'].apply_field_fixes()
    env['migration.fixes'].fix_kanban_templates()
    env['migration.fixes'].fix_partner_views()
