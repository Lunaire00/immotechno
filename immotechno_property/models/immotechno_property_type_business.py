# -*- coding: utf-8 -*-
from odoo import fields, models


class ImmotechnoBusinessType(models.Model):
    _name = "immotechno.business.type"
    _description = "immotechno commercial type"

    name = fields.Char(string="Name", translate=True)
    color = fields.Integer(string="color")
