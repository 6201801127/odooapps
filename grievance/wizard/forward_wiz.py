from odoo import fields, models, api, _ 

class ForwardGrievanceWizard(models.TransientModel):
    """Forward A grievance ticket if not resolve by default assign engineer for this kind of
    work i use this model """

    _name="forward.grievance.wizard"
    _description = "Forward grievance Wizard model"

    # -----------Default set category and category member default method-------------
    def _default_category_id(self):
        return self.env['grievance'].browse(self._context.get('active_id')).category_id
    def _default_team_member_id(self):
        return self.env['grievance'].browse(self._context.get('active_id')).team_member_id
    # ------------------------------end----------------------------------------------

    # ------------------------Define Field on Forwar_grievance_wizard table-----------------
    category_id = fields.Many2one(comodel_name='category', string='Category', default=_default_category_id)
    Cat_assign_member = fields.Many2one(comodel_name='hr.employee', string='Team Category Member', default=_default_team_member_id)
    #--------------------------End----------------------------------------------------------

    #----------------button to perfoam an action for set value on grievance form --------------------
    def forward_grievance_object_call(self):
        act_id = self.env['grievance'].browse(self._context.get('active_id'))
        act_id.team_id = self.category_id
        act_id.team_member_id = self.Cat_assign_member
    #-----------------------end---------------------------------------------------
       