# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class HrEmpolyeeInherit(models.Model):
    _inherit = 'hr.employee'

    headoffice_id = fields.Many2one('usc.whereabouts',
                                    string='Head Office', tracking=True)
    zone_id = fields.Many2one('usc.whereabouts', string='Zone', tracking=True)
    region_id = fields.Many2one('usc.whereabouts', string='Region', tracking=True)


    @api.onchange('zone_id')
    def _zone_onchange(self):
        for rec in self:
            rec.region_id = None
