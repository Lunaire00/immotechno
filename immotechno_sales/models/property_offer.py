# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class PropertyOffer(models.Model):
    _name = 'property.offer'
    _description ='property.offer'
    
    name = fields.Char(string='Offer Name')
    price = fields.Float(string='Offer Price')
    offer_date = fields.Date(string='Offer Date', default=fields.Date.today)
    down_payment = fields.Float(string='Down Payment')
    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    