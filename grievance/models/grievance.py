from odoo import models, fields, api, _

class Grievance(models.Model):
    _name = "grievance"
    _description = "Grievance management model"
    _rec_name = "category_id"

    def _get_default_stage_id(self):
        return self.env['stage'].search([], limit=1).id

    category_id = fields.Many2one(comodel_name="category", string='Category')
    team_id = fields.Many2one(comodel_name='category', string='Team')
    team_member_id = fields.Many2one(comodel_name='hr.employee',string='Team Member')
    sub_category_id = fields.Many2one(comodel_name="subcategory", string='Sub Category', default="Draft")
    priority = fields.Selection(selection=[
        ('0', _('Low')),
        ('1', _('Medium')),
        ('2', _('High')),
        ('3', _('Very High')),
    ], string='Priority', default='1')

    stage_id = fields.Many2one(comodel_name="stage", string="Stage", default=_get_default_stage_id, track_visibility='onchange')
    code = fields.Char(related='stage_id.code')
    description = fields.Text(string='Description')
    emp_name_id = fields.Many2one(comodel_name="hr.employee", string='Employee Name')
    emp_email = fields.Char(related="emp_name_id.work_email", string='Employee Email')
    emp_department = fields.Char(related="emp_name_id.department_id.name", string="Employee Department")
    emp_designation = fields.Char(related="emp_name_id.job_id.name", string='Employee Designation')
    word_limit = fields.Integer(string='Word Limit',default=100)
    phone = fields.Char(string='Phone')
    url_attach = fields.Char(string='Url')

    @api.onchange('description')
    def _check_grie_description(self):
        if self.description:
            self.word_limit = 500 - len(self.description)

    def raise_grievance_action_call(self):
        stage = self.env['stage'].sudo().search([('code', '=', 'N')], limit=1)
        self.stage_id = stage

    def accept_grievance_action_call(self):
        stage = self.env['stage'].sudo().search([('code', '=', 'IP')], limit=1)
        self.stage_id = stage
    
    def hold_grievance_action_call(self):
        stage = self.env['stage'].sudo().search([('code', '=', 'H')], limit=1)
        self.stage_id = stage

    def inprogress_grievance_action_call(self):
        stage = self.env['stage'].sudo().search([('code', '=', 'IP')], limit=1)
        self.stage_id = stage

    def close_grievance_action_call(self):
        stage = self.env['stage'].sudo().search([('code', '=', 'C')], limit=1)
        self.stage_id = stage

    def reject_grievance_action_call(self):
        stage = self.env['stage'].sudo().search([('code', '=', 'R')], limit=1)
        self.stage_id = stage
    def assign_spoc_action_call(self):
        pass

    def forward_grievance_method_call(self):
        action  = {
                    'name': "Grievance:Forward wizard",
                    'type': 'ir.actions.act_window',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'forward.grievance.wizard',
                    'view_id': self.env.ref('grievance.forward_grievance_wizard_view_form').id,
                    'target': 'new'
                }
        return action