from odoo import models, fields, api, _
import base64


class MockInterViewer(models.Model):
    _name = 'mock_interviewer.table'
    _description = 'Mock Interviewer'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Interviewer Name", required=True)
    account_name = fields.Char(string='Account Name')
    ifsc_code = fields.Char('IFSC Code')
    branch_name = fields.Char('Branch Name')
    account_holder = fields.Char('Account Holder Name')
    account_number = fields.Char('Account Number')
    interview_link = fields.Char('Interview Link')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    state = fields.Selection([
        ('draft', 'Draft'), ('done', 'Done')
    ], default='draft')

    def action_done(self):
        self.state = 'done'

    def return_to_draft(self):
        self.state = 'draft'


class LinkMockInterviewWizard(models.TransientModel):
    _name = 'link.mock_interview.wizard'
    _description = 'Link Mock Interview Wizard'

    interview_link_wizard = fields.Char('Interview Link')
    name = fields.Char('name')

    def action_done(self):
        print(self.interview_link_wizard)
