# -*- coding: utf-8 -*-
from odoo import models, fields, api


class RealEstate(models.Model):
    _name = 'room.type'
    _description = 'room.type'

    name = fields.Char(string='Name', required=True, translate=True)
    sequence = fields.Integer(string=('Sequence'))
