# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError

class Order(models.Model):
    _name = 'teashop.order'
    _description = "Arbitinės užsakimai"    

    name = fields.Datetime(default=fields.Datetime.now, string="Užsakimo data")
    tea_id = fields.Many2one("teashop.tea", required=True)
    customer_id = fields.Many2one("teashop.customer", required=True)
    state = fields.Selection([
        ('canceled', 'Atšauktas'),
        ('ordered', 'Užsakitas'),
        ('delivered', 'Pristatytas')
    ], default='ordered', group_expand="_expand_states")
    last_modification = fields.Datetime(default=fields.Datetime.now, readonly=True, string="Paskurtinis pakeitimas")

    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]
    
    def write(self, values):
        # helper to "YYYY-MM-DD"
        values['last_modification'] = fields.Datetime.now()

        return super(Order, self).write(values)

    def unlink(self):
        # self is a recordset
        for order in self:
           if order.state == 'delivered':
            raise UserError("Negalima ištrinti pristatyto užsakimo")

        return super(Order, self).unlink()
