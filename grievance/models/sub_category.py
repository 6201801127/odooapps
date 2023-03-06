from odoo import models, fields, api, _

class SubCategory(models.Model):
    _name = "subcategory"
    _description = "Grievance Sub Category"
    _rec_name = "name"
    name = fields.Char(string="Sub Category")
