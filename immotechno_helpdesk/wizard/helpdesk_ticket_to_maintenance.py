# -*- coding: utf-8 -*-

from odoo import api, Command, fields, models, _


class HelpdesckTicketConvertToMaintenance(models.TransientModel):
    _name = 'helpdesk.ticket.to.maintenance'
    _description = 'Convert Ticket to Maintenance'
    
    action_maintenance = fields.Selection([
                                           ('create', _('Create a new Maintenance')),
                                           ('exist', _('Link the Ticket to a Maintenance'))
                                          ], default='create')
    maintenance_id = fields.Many2one('maintenance.request', string='Maintenance')
    maintenance_id_domain = fields.Char(string='Maintenance Domain', compute='_compute_maintenance_id_domain')
    partner_id = fields.Many2one('res.partner', string='Tenant')
    ticket_id = fields.Many2one('helpdesk.ticket', string='Tickets', readonly=True)

    @api.depends('ticket_id.equipment_id')
    def _compute_maintenance_id_domain(self):
        for record in self:
            if record.ticket_id and record.ticket_id.equipment_id:
                record.maintenance_id_domain = [('equipment_id', '=', record.ticket_id.equipment_id.id)]
            else:
                record.maintenance_id_domain = []

    def convert_ticket_to_maintenance(self):
        if self.action_maintenance == 'create':
            maintenance = self.env['maintenance.request'].create({
            'name': self.ticket_id.name,
            'priority': self.ticket_id.priority,
            'equipment_id': self.ticket_id.equipment_id.id,
        })
        elif self.action_maintenance == 'exist':
            maintenance = self.maintenance_id
        maintenance.ticket_ids = [Command.link(self.ticket_id.id)]
