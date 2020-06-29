# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import UserError

class Work(models.Model):
    _name = 'workplan.work'
    _description = "Užduotis"    
    
    #data
    name = fields.Char("Darbo užduotis")
    info = fields.Text(string = "Darbo informacija")
    
    #relationship
    worker_id = fields.Many2one("res.users", string="Darbuotojai")
