# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ImmotechnoPropertyType(models.Model):
    _name = 'immotechno.property.type'
    _description = 'immotechno.property.type'

    name = fields.Char(string="Name", translate=True)
    color = fields.Integer(string="color")
