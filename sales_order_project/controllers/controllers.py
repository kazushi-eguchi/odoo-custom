# -*- coding: utf-8 -*-
# from odoo import http


# class SalesOrderProject(http.Controller):
#     @http.route('/sales_order_project/sales_order_project/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_order_project/sales_order_project/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_order_project.listing', {
#             'root': '/sales_order_project/sales_order_project',
#             'objects': http.request.env['sales_order_project.sales_order_project'].search([]),
#         })

#     @http.route('/sales_order_project/sales_order_project/objects/<model("sales_order_project.sales_order_project"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_order_project.object', {
#             'object': obj
#         })
