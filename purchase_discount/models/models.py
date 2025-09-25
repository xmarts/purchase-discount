from odoo import models, fields, api, tools
import logging

_logger = logging.getLogger(__name__)

class MigrationFixes(models.Model):
    _name = 'migration.fixes'
    _description = 'Odoo 18 Migration Fixes'

    @api.model
    def apply_field_fixes(self):
        """Apply fixes for duplicate field labels"""
        try:
            # Fix para campos product.template
            self._fix_product_template_fields()
            # Fix para campos product.product
            self._fix_product_product_fields()
            _logger.info("Field label fixes applied successfully")
            return True
        except Exception as e:
            _logger.error("Error applying field fixes: %s", e)
            return False

    def _fix_product_template_fields(self):
        """Fix duplicate labels in product.template"""
        template_fields = self.env['ir.model.fields'].search([
            ('model', '=', 'product.template'),
            ('name', 'in', ['x_studio_kva_1', 'x_studio_kva_2'])
        ])
        
        for field in template_fields:
            if field.name == 'x_studio_kva_1':
                field.field_description = 'KVA Principal'
            elif field.name == 'x_studio_kva_2':
                field.field_description = 'KVA Secundario'

    def _fix_product_product_fields(self):
        """Fix duplicate labels in product.product"""
        product_fields = self.env['ir.model.fields'].search([
            ('model', '=', 'product.product'),
            ('name', 'in', ['x_studio_kva_1', 'x_studio_kva_2'])
        ])
        
        for field in product_fields:
            if field.name == 'x_studio_kva_1':
                field.field_description = 'KVA Principal'
            elif field.name == 'x_studio_kva_2':
                field.field_description = 'KVA Secundario'

    @api.model
    def fix_kanban_templates(self):
        """Replace deprecated kanban-box templates with card"""
        try:
            kanban_views = self.env['ir.ui.view'].search([
                ('type', '=', 'kanban'),
                ('arch_db', 'ilike', 'kanban-box')
            ])
            
            for view in kanban_views:
                # Reemplazar kanban-box por card
                if 'kanban-box' in view.arch_db:
                    new_arch = view.arch_db.replace('t-name="kanban-box"', 't-name="card"')
                    new_arch = new_arch.replace('kanban-box', 'card')
                    view.write({'arch_db': new_arch})
            
            _logger.info("Kanban template fixes applied successfully")
            return True
        except Exception as e:
            _logger.error("Error fixing kanban templates: %s", e)
            return False
