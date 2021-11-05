from odoo import fields, models, api


class SaleCrm(models.Model):
    _inherit = "sale.order"
    lead_id = fields.Many2one(
        "crm.lead",
        string="lead",
    )
