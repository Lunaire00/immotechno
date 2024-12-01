# -*- coding: utf-8 -*-
from odoo import models, fields


class RoomTypeEntry(models.Model):
    _name = 'room.type.entry'
    _description = 'Room Type Entry'

    property_id = fields.Many2one('immotechno.property', string='Property', ondelete='cascade')
    quantity = fields.Integer(string='Quantity', default=1, required=True)
    room_id = fields.Many2one('room.type', string='Type of Room', required=True)
