# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerApproval(http.Controller):
#     @http.route('/partner_approval/partner_approval/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_approval/partner_approval/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_approval.listing', {
#             'root': '/partner_approval/partner_approval',
#             'objects': http.request.env['partner_approval.partner_approval'].search([]),
#         })

#     @http.route('/partner_approval/partner_approval/objects/<model("partner_approval.partner_approval"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_approval.object', {
#             'object': obj
#         })
