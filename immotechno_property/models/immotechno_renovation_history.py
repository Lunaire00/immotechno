# -*- coding: utf-8 -*-
from odoo import models, fields, api


class RenovationHistory(models.Model):
    _name = 'immo.renovation.history'
    _description = 'Renovation History'

    facture_ids = fields.Many2many(comodel_name='ir.attachment', string='Facture', help='Attach facture for this renovation')
    property_id = fields.Many2one('immotechno.property', string="Property", required=True, ondelete='cascade')
    renovation_date_start = fields.Date(string=" Start Renovation Date", required=True)
    renovation_date_end = fields.Date(string=" End Renovation Date", required=True)
    renovation_name = fields.Char(string="Renovation Name", required=True)
    renovation_price = fields.Float(string="Renovation Price (EUR)", required=True)
