from odoo import api, fields, models, _
from odoo.exceptions import UserError
import base64


class MockInterviewDaysStudentsList(models.Model):
    _name = 'interview.attend.students.list'
    _description = 'Students List'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date = fields.Datetime('Scheduled Date and Time', required=True)
    batch_id = fields.Many2one('logic.base.batch', string="Batch", required=True)
    students_list_ids = fields.One2many('attend.students.list', 'student_list_id', )
    interviewer_id = fields.Many2one('mock_interviewer.table', string="Interviewer", required=True)
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    coordinator_id = fields.Many2one('res.users', string="Coordinator", default=lambda self: self.env.user)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('interview', 'Interview Scheduled'),
    ], default='draft')

    def action_interview_schedule(self):
        self.state = 'interview'

    def copy_interview_link(self):
        print('jj')
        id = self.id
        int_bytes = id.to_bytes((id.bit_length() + 7) // 8, 'big')
        base64_string = base64.b64encode(int_bytes).decode('utf-8')
        print(base64_string, 'base64')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'link.mock_interview.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
            'context': {
                'default_interview_link_wizard': self.company_id.website + "/mock_interview/" + base64_string
            }
        }

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = 'Interview for ' + rec.batch_id.name

    @api.onchange('batch_id')
    def onchange_batch_id_for_students_list(self):
        students = self.env['logic.students'].search([('batch_id', '=', self.batch_id.id)])
        abc = []
        unlink_commands = [(3, child.id) for child in self.students_list_ids]
        self.write({'students_list_ids': unlink_commands})

        for i in students:
            res_list = {
                'name': i.id,

            }
            abc.append((0, 0, res_list))
        self.students_list_ids = abc


class AttendStudentsList(models.Model):
    _name = 'attend.students.list'

    name = fields.Many2one('logic.students', string='Name')
    student_list_id = fields.Many2one('interview.attend.students.list', string="Student List")

    @api.onchange('name')
    def onchange_name_for_students(self):

        print(self.env.context.get('parent_id'), 'oo')
        record = self.env['interview.attend.students.list'].browse(self.env.context.get('parent_id'))
        print(record, 'record')
