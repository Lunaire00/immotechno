# -*- coding: utf-8 -*-
from odoo import models, fields, api,_


class SaleOrder(models.Model):
    _inherit = 'sale.order'
 
    
    guarantor_ids = fields.Many2many('res.partner', 'immo_sale_guarantor_rel', string='Guarantor')
    offer_ids = fields.One2many('property.offer', 'sale_order_id', string='Offers')
    property_address = fields.Char(string ='Property Address')
    property_id = fields.Many2one('immotechno.property',
                                  string='Property',
                                  domain=[('status', '=', 'available')])
    property_owner_ids = fields.Many2many('res.partner', 'immo_sale_property_owner_rel', string='Property Owner')
    property_status_id = fields.Selection(related='property_id.status',string='Immotechno Property Status')
    sale_order_template_id = fields.Many2one('sale.order.template', string='Quotation Template')
    status_id = fields.Selection( string='Property Status', 
                                 selection=[('for_sale','Sale'),
                                            ('for_rent','Rent'),])
    tenant_ids= fields.Many2many('res.partner', 'immo_sale_tenant_rel', string='Tenant')

    @api.onchange('property_id')
    def _onchange_address(self):
        '''
        This method add the adress and owner based on the property_id
        if element for create an address existe 
            we creat it
        if owner existe 
            we create it
        '''
        if self.property_id:
            if self.property_id.street and self.property_id.city and self.property_id.zip:
                self.property_address = self.property_id.street + '\n' + \
                    self.property_id.city + '\n' + self.property_id.zip
            if self.property_id.property_owner_ids:
                self.property_owner_ids = self.property_id.property_owner_ids

    def property_change_rented_sale(self):
        if self.property_id:
            self.property_id.status = 'available'
        if self.property_id.status == 'rented':
            self.property_id.status = 'available'
        if self.property_id.status == 'for_sale':
            self.property_id.status = 'available'

    def _update_property_status(self):
        if self.property_id:
            if self.status_id == 'for_rent':
                self.property_id.status = 'rented'
            elif self.status_id == 'for_sale':
                self.property_id.status = 'for_sale'

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'cancel':
            self.property_change_rented_sale()
        if self.state == 'sale':
            self._update_property_status()
    
    @api.onchange('tenant_ids')
    def _onchange_tenant_ids(self):
        if self.env['ir.config_parameter'].sudo().get_param('immotechno_sales.is_tenant_garantor'):
            self.guarantor_ids = self.tenant_ids

    def change_on_subscription_state_cron(self):
        '''
        This method is used to change the status of the property 
        to 'rented' when the subscription state is churn
        It's call in a cron
        '''
        sale_orders = self.env['sale.order'].search(
            [('subscription_state', '=', '6_churn')])
        print(sale_orders)
        if sale_orders:
            for record in sale_orders:
                record.property_change_rented_sale()
                record.subscription_state = '7_upsell'

    def archive_house_sale_order(self):
        '''
        This method search all sale_orders where them state is sale
        then we mapped it for have ids of property
        And we use it for make a search based on these id to take just 
        when status is for_sale and active is false
        After that we archive all record we recieve
        This method is call in a cron 
        '''
        sale_orders = self.env['sale.order'].search([
            ('state', '=', 'sale')
        ])
        property_ids = sale_orders.mapped('property_id.id')
        sale_house = self.env['immotechno.property'].search([
            ('id', 'in', property_ids),
            ('status', '=', 'for_sale'),
            ('active', '=', True)
        ])
        for record in sale_house:
            record.active = False

    def _update_order_lines(self, record, status_id):
        '''
        This method creat 2 product. A sale and a rent. 
        We create a product for add and for remove 
        with these 2 products we search for a lines that we want remove
        and we search for a line that we want to add 
        we check if we have these 2 line. 
            If we have line_to_remove we unlink it 
            If we don't have a line_to_add we creat it 
        '''
        product_rent = self.env.ref('immotechno_sales.product_rent')
        product_sale = self.env.ref('immotechno_sales.product_sale')
        product_to_add = product_rent if status_id == 'for_rent' else product_sale
        product_to_remove = product_sale if status_id == 'for_rent' else product_rent
        existing_line_to_add = self.env['sale.order.line'].search([
            ('order_id', '=', record.id),
            ('product_id', '=', product_to_add.id)
        ])
        existing_line_to_remove = self.env['sale.order.line'].search([
            ('order_id', '=', record.id),
            ('product_id', '=', product_to_remove.id)
        ])
        if existing_line_to_remove:
            existing_line_to_remove.unlink()
        if not existing_line_to_add:
            self.env['sale.order.line'].create({
                'order_id': record.id,
                'product_id': product_to_add.id,
            })

    @api.model_create_multi
    def create(self, vals_list):
        '''
        The create will take our methods if we have the requierd value
        '''
        records = super(SaleOrder, self).create(vals_list)
        for record, vals in zip(records, vals_list):
            if vals.get('status_id'):
                self._update_order_lines(record, vals['status_id'])
            if vals.get('property_id'):
                record._onchange_address()
            if vals.get('state'):
                record._onchange_state()
        return records

    @api.model
    def write(self, vals):
        '''
        The create will take our methods if we have the requierd value
        '''
        result = super().write(vals)
        for rec in self:
            if vals.get('status_id'):
                self._update_order_lines(rec, vals['status_id'])
            if vals.get('property_id'):
                rec._onchange_address()
            if vals.get('state'):
                rec._onchange_state()
        return result

    @api.onchange('status_id')
    def _onchange_status_id(self):
        if self.status_id == 'for_sale':
            self.sale_order_template_id = self.env.ref(
                'immotechno_sales.quotation_template_sale')
        elif self.status_id == 'for_rent':
            self.sale_order_template_id = self.env.ref(
                'immotechno_sales.quotation_template_rent_1_year')
        else:
            self.sale_order_template_id = False
