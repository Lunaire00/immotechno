# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Building(models.Model):
    _name = 'building'
    _description = 'Building'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    address = fields.Char(string='Address')
    area = fields.Float(string='Area (m²)')
    city = fields.Char(string="City")
    construction_date = fields.Date(string='Construction Date')
    country_id = fields.Many2one('res.country', string="Country")
    currency_id = fields.Many2one('res.currency', string="Currency")
    elevator_installed = fields.Boolean(string='Elevator Installed', default=False)
    estimated_value = fields.Monetary(string='Estimated Value', currency_field='currency_id')
    image = fields.Binary()
    name = fields.Char(string='Name', required=True)
    notes = fields.Text(string='Additional Notes')
    number_of_floor = fields.Integer(string="Number of floors")
    property_ids = fields.One2many('immotechno.property', 'type_building_id', string='Properties')
    rented_ratio = fields.Char(string="Rented Ratio", compute='_compute_rented_ratio', store=False)
    sequence = fields.Integer(string='Sequence')
    state_id = fields.Many2one('res.country.state', string="State")
    smart = fields.Char(string="Smart")
    street = fields.Char(string="Street")
    zip = fields.Char(string="Zip code")

    def _compute_rented_ratio(self):
        for building in self:
            total_properties = len(building.property_ids)
            rented_properties = len(building.property_ids.filtered(
                lambda p: p.status == 'rented'))
            
            if total_properties > 0:
                percentage = round((rented_properties / total_properties) * 100)
                building.rented_ratio = f"{rented_properties}/{total_properties} ({percentage}%)"
            else:
                building.rented_ratio = "0/0 (0%)"
