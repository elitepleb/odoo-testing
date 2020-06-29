# -*- coding: utf-8 -*-
from odoo import fields, models

class Customer(models.Model):
    _name = 'teashop.customer'
    _description = "Arbitinės pirkėjas"    

    name = fields.Char("Pirkėjo vardas", required=True)
    email = fields.Char(help="Gauti naujienas")
    order_ids = fields.One2many("teashop.order","customer_id", string="Užsakimai")
