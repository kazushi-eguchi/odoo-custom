# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Purchase_Order_In_Lead(models.Model):
    _inherit = "crm.lead"
    purchase_id = fields.One2many(
        comodel_name="purchase.order",
        inverse_name="lead_id",
        string='purchase'
    )
    po_count = fields.Integer(string="PO Count", compute="_compute_po_count")

    def _compute_po_count(self):
        for rec in self:
            po_count = self.env['purchase.order'].search_count([('lead_id', '=', rec.id)])
            rec.po_count = po_count

    def action_open_po(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'purchase',
            'res_model': 'purchase.order',
            'domain': [('lead_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_lead_id': self.id,
            }
        }

    def create_lead(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_purchase.order': self.id,
            }
        }


#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
