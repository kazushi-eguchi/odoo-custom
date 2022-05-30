from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order"

    image_count = fields.Integer(compute="_image_count")

    def _image_count(self):
        for rec in self:
            count = 0
            for l in self.order_line:
                count += l.item_purchase_image_count
            rec.image_count = count
