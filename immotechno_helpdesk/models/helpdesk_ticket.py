# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    equipment_id = fields.Many2one('maintenance.equipment', string='Equipment')
    equipment_id_domain = fields.Char(string='Equipment Domain', compute='_compute_equipment_id_domain')
    maintenance_id = fields.Many2one('maintenance.request', string='Maintenance')
    partner_id = fields.Many2one('res.partner', string='Tenant', tracking=True, index=True)
    property_id = fields.Many2one('immotechno.property', string='Property')
    property_id_domain = fields.Char(string='Property Domain', compute='_compute_property_id_domain')

    @api.depends('partner_id')
    def _compute_property_id_domain(self):
        for record in self:
            if record.partner_id:
                record.property_id_domain = [('tenant_ids', 'in', self.partner_id.id)]
            else:
                record.property_id_domain = []

    @api.depends('property_id')
    def _compute_equipment_id_domain(self):
        for record in self:
            if record.property_id:
                record.equipment_id_domain = [('property_id', '=', record.property_id.id)]
            else:
                record.equipment_id_domain = []

    def action_convert_ticket_to_maintenance(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Convert Ticket to Maintenance'),
            'res_model': 'helpdesk.ticket.to.maintenance',  
            'view_mode': 'form',
            'target': 'new',  
            'context': {
                'default_ticket_id': self.id,  
                'dialog_size': 'medium',  
            }
        }
