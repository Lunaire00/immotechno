# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ImmoTechnoSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_hide_icon_kanban = fields.Boolean(string="Hide Number Rooms Icons",help="Hide the coin icons")

    def set_values(self):
        """
        Override the set_values method to update the 'is_hide_rooms' field
        in all 'immotechno.property' records based on the value of 'is_hide_icon_kanban'.
        """
        super(ImmoTechnoSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            'immotechno_property.is_hide_icon_kanban', self.is_hide_icon_kanban)
        properties = self.env['immotechno.property'].search([])
        for property in properties:
            property.sudo().write({'is_hide_rooms': self.is_hide_icon_kanban})

    @api.onchange('is_hide_icon_kanban')
    def _onchange_hide_rooms(self):
        self.set_values()

    @api.model
    def get_values(self):
        res = super(ImmoTechnoSettings, self).get_values()
        res.update(
            is_hide_icon_kanban=self.env['ir.config_parameter'].sudo().get_param(
                'immotechno_property.is_hide_icon_kanban', default=False)
        )
        return res
