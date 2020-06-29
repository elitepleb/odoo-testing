# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError


class Tea(models.Model):
    _name = 'teashop.tea'
    _description = "Arbitinės arbatos"    

    name = fields.Char("Arbatos pavadinimas")
    price = fields.Float(string="Kaina")
    order_ids = fields.One2many("teashop.order", "tea_id", string="Užsakimai")
    order_count = fields.Integer(compute='_get_total_sold', store=True, string="Iš viso perduota")
    number_in_stock = fields.Integer(string="Arbatos kiekis")

    @api.depends('order_ids')
    def _get_total_sold(self):
        for plant in self:
            plant.order_count = len(plant.order_ids)

    @api.constrains('order_count', 'number_in_stock')
    def _check_available_in_stock(self):
        for tea in self:
            if tea.number_in_stock and tea.order_count > tea.number_in_stock:
                raise UserError("Yra tik %s %s arbatos parduotuvėje, bet %s bandomi užsakyti"
                      % (tea.number_in_stock, tea.name, tea.order_count))

