# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Purchase_Order_In_Project(models.Model):
    _inherit = "project.project"
    purchase_ids = fields.One2many(
        comodel_name="purchase.order",
        inverse_name="project_id",
        string='purchase'
    )
    po_count = fields.Integer(string="PO Count", compute="_compute_po_count")

    def _compute_po_count(self):
        for rec in self:
            po_count = self.env['purchase.order'].search_count([('project_id', '=', rec.id)])
            rec.po_count = po_count

    def action_open_po(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'purchase',
            'res_model': 'purchase.order',
            'domain': [('project_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {
                'default_project_id': self.id,
            }
        }
