# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

class Plan(models.Model):
    _name = 'workplan.plan'
    _inherit = ['mail.thread']
    _description = "Planai"    
    
    #data
    name = fields.Char("Darbo planas")
    state = fields.Selection([
        ('planning', 'Planas'),
        ('doing', 'Daroma'),
        ('done', 'Padaryta')
    ], default='planning', group_expand="_expand_states")
    last_modification = fields.Datetime(default=fields.Datetime.now, readonly=True, string="Paskurtinis pakeitimas")
    finish = fields.Datetime(string="Plano terminas")
    
    #relationship
    work_ids = fields.Many2many("workplan.work", required=True, string="Darbai")
    leader_id = fields.Many2one("res.partner", required=True, string="Vadovas")
    
    #functions
    def _expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]
    
    def write(self, values):
        values['last_modification'] = fields.Datetime.now()
        
        if values['state'] != "planning":
            values['finish'] = fields.Datetime.now() + relativedelta(day=1)

        else:
            values['finish'] = None

        return super(Plan, self).write(values)
