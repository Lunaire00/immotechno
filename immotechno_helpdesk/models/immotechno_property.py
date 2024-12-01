from odoo import models, fields, api, _

class ImmoTechno(models.Model):
    _inherit = 'immotechno.property'

    equipment_ids = fields.One2many('maintenance.equipment','property_id',string='Equipements')
    equipment_count = fields.Integer(string='Count', compute='_compute_equipment_count', store=True)
    maintenance_count = fields.Integer(string='Count of Maintenances', compute='_compute_maintenance_count', store=False)

    def action_view_equipment(self):
        """Opens a window to view all the equipment associated with the property."""
        
        return {
            'name':'Equipements',
            'type': 'ir.actions.act_window',
            'res_model': 'maintenance.equipment',
            'view_mode': 'tree,form',
            'domain': [('property_id', '=', self.id)],
            'context': {
                'default_property_id': self.id,
            },
        }

    def action_view_maintenance(self):
        """Opens a window to view all the maintenance requests associated with the property."""
        equipment_ids = self.env['maintenance.equipment'].search([
            ('property_id', '=', self.id),
        ])
        return {
            'name':'Maintenance',
            'type': 'ir.actions.act_window',
            'res_model': 'maintenance.request',
            'view_mode': 'tree,form',
            'domain': [('equipment_id', 'in', equipment_ids.ids)],
        }
        
    @api.depends('equipment_ids')
    def _compute_maintenance_count(self):
        """
        Search equipement liked to property
        Search maintenace liked to equipement we get
        count that maintenance 
        """
        for record in self:
            equipment_ids = self.env['maintenance.equipment'].search([
                ('property_id', '=', record.id),
            ])
            maintenance_ids = self.env['maintenance.request'].search([
                ('equipment_id', 'in', equipment_ids.ids)
            ])
            record.maintenance_count = len(maintenance_ids)

    @api.depends('equipment_ids')
    def _compute_equipment_count(self):
        """Updates the equipment count based on the number of related equipment."""
        for record in self:
            record.equipment_count = len(record.equipment_ids)
