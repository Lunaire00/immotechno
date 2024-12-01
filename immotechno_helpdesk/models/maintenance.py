# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class MaintenanceEquipment(models.Model):
    _inherit = ['maintenance.equipment']

    building_id = fields.Many2one('building', string='Building')
    is_building = fields.Boolean(string="In building")
    property_id = fields.Many2one('immotechno.property', string='Property',tracking=True)
    rel_type_building_id = fields.Many2one(related='property_id.type_building_id', string='Rel Type Of Building')
    rel_type_property_id = fields.Many2one(related='property_id.type_property_id', string='Type of Property')
    rel_tenant_ids = fields.Many2many(related='property_id.tenant_ids', string='Tenant')


class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    ticket_ids = fields.One2many('helpdesk.ticket', 'maintenance_id', string='Tickets')
    property_maintenance_id = fields.Many2one('immotechno.property', string='Property')
    ticket_count = fields.Integer(string='Ticket Count', compute='_compute_ticket_count', store=True)

    def action_view_ticket(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tickets',
            'res_model': 'helpdesk.ticket',
            'view_mode': 'tree,form,kanban',
            'domain': [('maintenance_id', '=', self.id)],
            'context': {
                'default_maintenance_id': self.id,
            },
        }

    @api.depends('ticket_ids')
    def _compute_ticket_count(self):
        for record in self:
           record.ticket_count = len(record.ticket_ids)
