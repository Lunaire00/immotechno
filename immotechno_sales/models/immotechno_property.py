# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ImmotechnoProperty(models.Model):
    _inherit = 'immotechno.property'

    guarantor_ids = fields.Many2many('res.partner', 'immo_garantor_rel', string="Garantor", compute='_compute_sale_order')
    sale_count = fields.Integer(string='sale_count', compute='_compute_sale_count')
    sale_order_id = fields.Many2one(comodel_name='sale.order', string="Sale Order")
    payer_id = fields.Many2one('res.partner', string="Payer", compute='_compute_sale_order')
    tenant_ids = fields.Many2many('res.partner', string="Tenant", compute='_compute_sale_order')

    def action_view_sale_order(self):
        sale_order = self.env['sale.order'].search([('property_id', '=', self.id)], limit=1)
        if sale_order:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'view_mode': 'form',
                'res_id': sale_order.id,
                'context': {
                    'default_property_id': self.id,
                },
            }
        else:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'view_mode': 'tree,form',
                'domain': [('property_id', '=', self.id)],
                'context': {
                    'default_property_id': self.id,
                },
            }

    @api.depends('sale_order_id')
    def _compute_sale_order(self):
        for record in self:
            sale_order = self.env['sale.order'].search([('property_id', '=', record.id), (
                'state', '!=', 'cancel'), ('subscription_state', '!=', '6_churn')], limit=1)
            if record:
                self.tenant_ids = sale_order.tenant_ids
                self.payer_id = sale_order.partner_id
                self.guarantor_ids = sale_order.guarantor_ids

    @api.depends('sale_order_id')
    def _compute_sale_count(self):
        for record in self:
            sale_orders = self.env['sale.order'].search([('property_id', '=', record.id), ('state', '!=', 'cancel'), ('subscription_state', '=', '3_progress')])
            record.sale_count = len(sale_orders)
