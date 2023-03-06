from odoo import models, fields, api, _

class Category(models.Model):
    _name = "category"
    _description = "Grievance Category Model"
    _rec_name = "name"

    name = fields.Char(string='Category')
    first_level_ids = fields.Many2many(comodel_name="res.users", string="SPOC Level-1", relation="grievance_category_user_rel", column1="category_id", column2="user_id")
    second_level_ids = fields.Many2many(comodel_name="res.users", string="SPOC Level-2", relation="gcategory_users_rel", column1="category2_id", column2="user2_id")
    is_random_assign = fields.Boolean(string="Is Random Assign")
    subcategory_ids = fields.Many2many(comodel_name="subcategory", string="Sub category", relation="grievance_category_rel", column1="griev_category_id", column2="griev_subcategory_id")
    assigned_ticket_count = fields.Integer(string="Assigned ticket", compute='_compute_assigned_ticket_count')
    unassigned_ticket_count = fields.Integer(string='Unassigned Ticket',compute='_compute_unassigned_ticket_count')
    todo_open_ticket_count = fields.Integer(string='Open Ticket', compute='_compute_open_ticket_count')
    todo_in_progress_ticket_count = fields.Integer(string='In Progress Ticket',compute='_compute_todo_in_progress_ticket_count')
    todo_on_hold_ticket_count = fields.Integer(string='On Hold Ticket', compute='_compute_on_hold_ticket_count')
    todo_completed_ticket_count = fields.Integer(string='Completed Ticket',compute='_compute_todo_completed_ticket_count')
    todo_rejected_ticket_count = fields.Integer(string='Rejected Ticket', compute='_compute_todo_rejected_ticket_count')
    priory_ticket_count = fields.Integer(string='High Priority Ticket',compute='_compute_priority')
    grievance_ticket_ids = fields.One2many(comodel_name='grievance',inverse_name='category_id',string='Grievance Ticket')

    @api.depends('grievance_ticket_ids.stage_id')
    def _compute_open_ticket_count(self):
        for record in self:
            ticket_count_open = self.env["grievance"].search_count([('code', 'in',['D','N','IP']),('category_id','=', record.id)])
            print('ticket_count_open',ticket_count_open)
            if ticket_count_open:
                record.todo_open_ticket_count = ticket_count_open
            else:
                record.todo_open_ticket_count = False
    
    @api.depends('grievance_ticket_ids.code')
    def _compute_todo_in_progress_ticket_count(self):
        for record in self:
            in_progress_ticket_count = self.env["grievance"].search_count([('code', 'in',['IP']),('category_id','=', record.id)])
            if in_progress_ticket_count:
                record.todo_in_progress_ticket_count = in_progress_ticket_count
            else:
                record.todo_in_progress_ticket_count = False

    @api.depends('grievance_ticket_ids.code')
    def _compute_todo_completed_ticket_count(self):
        for record in self:
            completed_ticket_count = self.env["grievance"].search_count([('code', 'in',['C']),('category_id','=', record.id)])
            if completed_ticket_count:
                record.todo_completed_ticket_count = completed_ticket_count
            else:
                record.todo_completed_ticket_count = False
    
    @api.depends('grievance_ticket_ids.code')
    def _compute_todo_rejected_ticket_count(self):
        for record in self:
            rejected_ticket_count = self.env["grievance"].search_count([('code', 'in',['R']),('category_id','=', record.id)])
            if rejected_ticket_count:
                record.todo_rejected_ticket_count = rejected_ticket_count
            else:
                record.todo_rejected_ticket_count = False

    @api.depends('grievance_ticket_ids.priority')
    def _compute_priority(self):
        for record in self:
            ticket_count_priority = self.env["grievance"].search_count([('priority','=','3'),('category_id','=',record.id)])
            if ticket_count_priority:
                record.priory_ticket_count = ticket_count_priority
            else:
                record.priory_ticket_count = False
    @api.depends('grievance_ticket_ids.code')
    def _compute_on_hold_ticket_count(self):
        for record in self:
            on_hold_ticket_count = self.env["grievance"].search_count([('code','=','H'),('category_id','=',record.id)])
            if on_hold_ticket_count:
                record.todo_on_hold_ticket_count = on_hold_ticket_count
            else:
                record.todo_on_hold_ticket_count = False
   
    @api.depends('grievance_ticket_ids.team_id','grievance_ticket_ids.team_member_id')
    def _compute_assigned_ticket_count(self):
        for record in self:
            assigned_count = self.env["grievance"].search_count([('team_id', '!=',False),('category_id','=', record.id)])
            print('ticket_count_open',assigned_count)
            if assigned_count:
                record.assigned_ticket_count = assigned_count
            else:
                record.assigned_ticket_count = False
    @api.depends('grievance_ticket_ids.team_id','grievance_ticket_ids.team_member_id')
    def _compute_unassigned_ticket_count(self):
        for record in self:
            unassigned_count = self.env["grievance"].search_count([('team_id', '=',False),('category_id','=', record.id)])
            print('ticket_count_open',unassigned_count)
            if unassigned_count:
                record.unassigned_ticket_count = unassigned_count
            else:
                record.unassigned_ticket_count = False