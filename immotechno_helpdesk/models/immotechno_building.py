# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Building(models.Model):
    _inherit = 'building'

    building_count = fields.Integer(string='Count', compute='_compute_building_count', store=True)
    building_ids = fields.One2many('maintenance.equipment', 'building_id', string='Equipments')

    def action_view_building(self):
        """Opens a window to view all the equipment associated with the building."""
        return {
            'name':'Building',
            'type': 'ir.actions.act_window',
            'res_model': 'maintenance.equipment',
            'view_mode': 'tree,form',
            'domain': [('building_id', '=', self.id)],
            'context': {
                'default_building_id': self.id,
            },
        }

    @api.onchange('building_ids')
    def _onchange_building_ids(self):
        """Updates the building count whenever the building list changes."""
        for record in self:
            record.building_count = len(record.building_ids)

    @api.depends('building_ids')
    def _compute_building_count(self):
        """Updates the building count based on the number of related equipment."""
        for record in self:
            record.building_count = len(record.building_ids)
