from odoo import models, fields, api, _


class MockInterview(models.Model):
    _name = 'logic.mock_interview'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Mock Interview'

    student_name = fields.Char(string='Student Name', required=True)
    communication_skill = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Communication Skill',
    )
    language_skill = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Language Skill',
    )
    presentation_skill = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Presentation Skill',
    )
    confidence_level = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Confidence Level',
    )
    body_language = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Body Language',
    )
    dressing_pattern = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Dressing Pattern',
    )
    attitude = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Attitude',
    )
    quality_of_resume = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Quality of Resume',
    )
    friendliness = fields.Selection(
        [('0', 'None'), ('1', 'Poor'), ('2', 'Fair'), ('3', 'Good'), ('4', 'Very Good'), ('5', 'Excellent')],
        string='Friendliness',
    )
    interviewer = fields.Many2one('mock_interviewer.table', string='Interviewer')

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = 'Mock interview for ' + rec.student_name
