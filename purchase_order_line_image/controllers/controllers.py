# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderLineImage(http.Controller):
#     @http.route('/purchase_order_line_image/purchase_order_line_image/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_line_image/purchase_order_line_image/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_line_image.listing', {
#             'root': '/purchase_order_line_image/purchase_order_line_image',
#             'objects': http.request.env['purchase_order_line_image.purchase_order_line_image'].search([]),
#         })

#     @http.route('/purchase_order_line_image/purchase_order_line_image/objects/<model("purchase_order_line_image.purchase_order_line_image"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_line_image.object', {
#             'object': obj
#         })
