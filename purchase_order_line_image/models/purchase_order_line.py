from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    item_purchase_image_ids = fields.Many2many("item.purchase_image", string="Item Images", copy=True)
    item_purchase_image_count = fields.Integer(
        "Image Count", compute="_compute_item_image_count"
    )

    def _compute_item_image_count(self):
        for line in self:
            line.item_purchase_image_count = len(line.item_purchase_image_ids)

    def action_get_item_purchase_image_view(self):
        self.ensure_one()
        res = self.env["ir.actions.act_window"]._for_xml_id(
            "purchase_order_line_image.action_item_image"
        )
        res["domain"] = [("purchase_line_ids", "in", self.id)]
        res["context"] = {
            "default_name": self.name,
            "default_product_id": self.product_id.id if self.product_id else False,
            "default_purchase_line_ids": [(4, self.id)],
        }
        return res
