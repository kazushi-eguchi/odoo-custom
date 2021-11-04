# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import exceptions
from odoo import api, models, _
from datetime import date


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_project_vals(self):
        self.ensure_one()
        name = u" %s - %s - %s" % (
            self.partner_id.name,
            date.today().year,
            self.name)
        return {
            'user_id': self.user_id.id,
            'name': name,
            'partner_id': self.partner_id.id,
        }

    def action_create_project(self):
        project_obj = self.env['project.project']
        for order in self:
            if order.project_id:
                raise exceptions.UserError(_(
                    'There is a project already related with this sale order.'
                ))
            vals = order._prepare_project_vals()
            project = project_obj.create(vals)
            print(project.analytic_account_id.id)
            order.write({
                'project_id': project.id
            })
        return True
