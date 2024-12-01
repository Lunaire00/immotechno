# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ImmoTechnoSaleSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_tenant_garantor = fields.Boolean(string="Tenant is Garantor")

    def set_values(self):
        super(ImmoTechnoSaleSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('immotechno_sales.is_tenant_garantor', self.is_tenant_garantor)

    @api.model
    def get_values(self):
        res = super(ImmoTechnoSaleSettings, self).get_values()
        res.update(
            is_tenant_garantor=self.env['ir.config_parameter'].sudo().get_param('immotechno_sales.is_tenant_garantor', default=False)
        )
        return res
