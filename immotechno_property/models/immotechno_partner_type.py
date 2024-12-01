# -*- coding: utf-8 -*-
from odoo import fields, models


class ImmotechnoPartnerType(models.Model):
    _name = "immotechno.partner.type"
    _description = 'Partner Type'

    name = fields.Char(string="Name", required=True, translate=True)
