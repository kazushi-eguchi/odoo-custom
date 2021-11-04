# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderInLead(http.Controller):
#     @http.route('/purchase_order_in_lead/purchase_order_in_lead/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_in_lead/purchase_order_in_lead/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_in_lead.listing', {
#             'root': '/purchase_order_in_lead/purchase_order_in_lead',
#             'objects': http.request.env['purchase_order_in_lead.purchase_order_in_lead'].search([]),
#         })

#     @http.route('/purchase_order_in_lead/purchase_order_in_lead/objects/<model("purchase_order_in_lead.purchase_order_in_lead"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_in_lead.object', {
#             'object': obj
#         })
