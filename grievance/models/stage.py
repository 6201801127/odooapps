from odoo import models, fields, api, _

class Stage(models.Model):
    _name ="stage"
    _description ="Grievance Stage"
    _rec_name = "name"
    _order = 'sequence asc'

    name = fields.Char(string='Stage')
    code = fields.Char(string="Stage Code")
    sequence = fields.Integer(string="Sequence")