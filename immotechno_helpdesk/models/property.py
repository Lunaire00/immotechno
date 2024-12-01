# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ImmoTechnoProperty(models.Model):

    _inherit = 'immotechno.property'

    equipement_ids = fields.One2many('maintenance.equipment','property_id',string=' ',readonly=True)