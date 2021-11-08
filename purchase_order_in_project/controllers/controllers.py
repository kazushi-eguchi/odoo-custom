# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderInProject(http.Controller):
#     @http.route('/purchase_order_in_project/purchase_order_in_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_in_project/purchase_order_in_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_in_project.listing', {
#             'root': '/purchase_order_in_project/purchase_order_in_project',
#             'objects': http.request.env['purchase_order_in_project.purchase_order_in_project'].search([]),
#         })

#     @http.route('/purchase_order_in_project/purchase_order_in_project/objects/<model("purchase_order_in_project.purchase_order_in_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_in_project.object', {
#             'object': obj
#         })
