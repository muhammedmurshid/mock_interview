from odoo import api, fields, models, _


class MockInterviewerRate(models.Model):
    _name = 'mock.interviewer.rate'
    _description = 'Interviewer Rate'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Many2one('mock_interviewer.table', 'Interviewer Name')
    rate = fields.Float('Rate')
