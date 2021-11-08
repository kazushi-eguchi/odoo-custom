from odoo import fields, models, api


class PurchaseInherit(models.Model):
    _inherit = 'purchase.order'
    project_id = fields.Many2one(
        "project.project",
        string="project",
    )
