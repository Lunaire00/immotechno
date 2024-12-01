# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ImmoTechno(models.Model):
    _name = 'immotechno.property'
    _description = 'immotechno.property'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    active = fields.Boolean(string='active', default=True)
    adress = fields.Char(string="Adress")
    air_conditioning = fields.Boolean(string="Air Conditioning")
    business_or_residential = fields.Selection([
        ('residential', 'Residential'),
        ('business', 'Business')
    ], default='residential')
    city = fields.Char(string="City")
    construction_year = fields.Integer(string="Construction Year")
    country_id = fields.Many2one('res.country', string="Country")
    currency_id = fields.Many2one('res.currency', string="Currency")
    disability_access = fields.Boolean(string="Disability Access")
    energy_rating = fields.Selection([
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G')
    ], string="Energy Rating")
    estimated_value = fields.Monetary(
        string="Estimated Value", currency_field='currency_id')
    exterior_finish = fields.Selection([
        ('brick', 'Brick'),
        ('concrete', 'Concrete'),
        ('wood', 'Wood'),
        ('other', 'Other')
    ], string="Exterior Finish")
    flooring_finish = fields.Selection([
        ('tiles', 'Tiles'),
        ('parquet', 'Parquet'),
        ('carpet', 'Carpet'),
        ('concrete', 'Concrete'),
        ('other', 'Other')
    ], string="Flooring Finish")
    garden_area = fields.Float(string="Garden Area (m²)")
    guarantor_ids = fields.Many2many('res.partner', string="Garantor")
    has_attic = fields.Boolean(string="Has Attic")
    has_basement = fields.Boolean(string="Has Basement")
    has_elevator = fields.Boolean(string="Elevator Available")
    has_garden = fields.Boolean(string="Has Garden")
    has_pool = fields.Boolean(string="Has Pool")
    has_terrace = fields.Boolean(string="Has Terrace")
    heating_type = fields.Selection([
        ('electric', 'Electric'),
        ('gas', 'Gas'),
        ('wood', 'Wood'),
        ('oil', 'Oil'),
        ('other', 'Other')
    ], string="Heating Type")
    interior_finish = fields.Selection([
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('luxury', 'Luxury')
    ], string="Interior Finish")
    is_furnished = fields.Boolean(string="Furnished")
    is_furnished_price = fields.Monetary(
        string="Equipement Price", currency_field='currency_id')
    is_hide_rooms = fields.Boolean(default=False)
    is_kitchen_equipped = fields.Boolean(string="Is Kitchen Equipped")
    is_pet_allowed = fields.Boolean(string="Pets Allowed")
    kitchen_area = fields.Float(string="Kitchen Area (m²)")
    living_room_area = fields.Float(string="Living Room Area (m²)")
    main_floor_type = fields.Selection([
        ('tiles', 'Tiles'),
        ('parquet', 'Parquet'),
        ('carpet', 'Carpet'),
        ('concrete', 'Concrete'),
        ('other', 'Other')
    ], string="Main Floor Type")
    name = fields.Char(string="Name", required=True)
    number_of_bathrooms_id = fields.Many2one(
        'room.type', string="Number of Bathrooms")
    number_of_warehouses_id = fields.Many2one(
        'room.type', string="Number of Warehouses")
    number_of_bedrooms_id = fields.Many2one(
        'room.type', string="Number of Bedrooms")
    number_of_floors = fields.Integer(string="Number of Floors")
    orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')], string="Orientation")
    parking = fields.Boolean(string="Parking")
    payer_id = fields.Many2one('res.partner', string="Customer")
    photo = fields.Binary()
    property_owner_ids = fields.Many2many('res.partner',
                                          'immo_property_owner_rel',
                                          string="Property Owners",
                                          )
    plan_ids = fields.Many2many(
        comodel_name='ir.attachment', string='Plans', help='Attach plans for this property')
    price = fields.Float(string='Selling Price', digits=(16, 0))
    proximity_to_schools = fields.Float(string="Proximity to Schools (km)")
    proximity_to_shops = fields.Float(string="Proximity to Shops (km)")
    public_transport_distance = fields.Float(
        string="Distance to Public Transport (km)")
    renewable_energy_sources = fields.Boolean(
        string="Renewable Energy Sources")
    renovation_history_ids = fields.One2many(
        'immo.renovation.history', 'property_id', string="Renovation History")
    room_entry_ids = fields.One2many(
        'room.type.entry', 'property_id', string='Room Entries')
    show_price = fields.Boolean(compute="_compute_show_price", store=True)
    state_id = fields.Many2one('res.country.state', string="State")
    status = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('for_sale', 'For Sale')
    ], string='Status', default='available')
    street = fields.Char(string="Street")
    surface = fields.Float(string="Surface Area (m²)", digits=(16, 0))
    tenant_ids = fields.Many2many(
        'res.partner', 'immo_property_tenant_rel', string="Tenant")
    thermal_insulation = fields.Selection([
        ('good', 'Good'),
        ('average', 'Average'),
        ('poor', 'Poor')
    ], string="Thermal Insulation")
    total_bathrooms = fields.Integer(
        string='Total Bathrooms', compute='_compute_total_bathrooms', store=True)
    total_rooms = fields.Integer(
        string='Total Rooms', compute='_compute_total_rooms', store=True)
    total_warehouses = fields.Integer(
        string='Total Warehouse', compute='_compute_total_warehouses', store=True)
    type_building_id = fields.Many2one('building', string="Building")
    type_business_id = fields.Many2one(
        'immotechno.business.type', string="Type of business")
    type_property_id = fields.Many2one(
        'immotechno.property.type', string="Type of property")
    type_room_id = fields.Many2one('room.type', string="Number of rooms")
    smart = fields.Char(string="Smart")
    window_quality = fields.Selection([
        ('single', 'Single Glazing'),
        ('double', 'Double Glazing'),
        ('triple', 'Triple Glazing')
    ], string="Window Quality")
    zip = fields.Char(string="Zip code")


    @api.depends('room_entry_ids')
    def _compute_total_rooms(self):
        bedroom_type_id = self.env.ref('immotechno_property.room_type_1').id
        for record in self:
            record.total_rooms = sum(
                entry.quantity for entry in record.room_entry_ids if entry.room_id.id == bedroom_type_id)

    @api.depends('room_entry_ids')
    def _compute_total_bathrooms(self):
        bathroom_type_id = self.env.ref('immotechno_property.room_type_2').id
        for record in self:
            record.total_bathrooms = sum(
                entry.quantity for entry in record.room_entry_ids if entry.room_id.id == bathroom_type_id)

    @api.depends('room_entry_ids')
    def _compute_total_warehouses(self):
        warehouse_type_id = self.env.ref('immotechno_property.room_type_6').id
        for record in self:
            record.total_warehouses = sum(
                entry.quantity for entry in record.room_entry_ids if entry.room_id.id == warehouse_type_id)

    def action_print_property_report(self):
        return self.env.ref('immotechno_property.property_report_pdf').report_action(self)
