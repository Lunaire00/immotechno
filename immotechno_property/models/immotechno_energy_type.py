# -*- coding: utf-8 -*-
from odoo import fields, models


class ImmotechnoEnergyType(models.Model):
    _name = "immotechno.energy.type"
    _description = "immotechno energy type"

    name = fields.Char(string="Name")
