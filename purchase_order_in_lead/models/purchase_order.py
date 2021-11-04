from odoo import fields, models, api


class PurchaseInherit(models.Model):
    _inherit = 'purchase.order'
    lead_id = fields.Many2one(
        "crm.lead",
        string="lead",
    )
