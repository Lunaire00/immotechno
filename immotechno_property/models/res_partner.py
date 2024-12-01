# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_type_ids = fields.Many2many("immotechno.partner.type")
