# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class ImmoTechnoBuilding(models.Model):

    _inherit = 'building'

    equipement_ids = fields.One2many('maintenance.equipment','building_id',string=' ',readonly=True)
