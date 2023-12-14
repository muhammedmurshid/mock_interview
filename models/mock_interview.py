from odoo import models, fields, api, _


class MockInterview(models.Model):
    _name = 'logic.mock_interview'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Mock Interview'

    student_name = fields.Many2one('logic.students', string='Student Name', required=True)
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
    coordinator = fields.Many2one('res.users', string='Coordinator')
    state = fields.Selection([
        ('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'),
    ], default='draft', tracking=True)
    date = fields.Date('Date', default=lambda self: fields.Date.context_today(self))

    def action_done(self):
        student = self.env['logic.students'].search([('id', '=', self.student_name.id)])
        student.mock_date = self.date
        student.mock_communication_skill = self.communication_skill
        student.mock_language_skill = self.language_skill
        student.mock_presentation_skill = self.presentation_skill
        student.mock_confidence_level = self.confidence_level
        student.mock_body_language = self.body_language
        student.mock_dressing_pattern = self.dressing_pattern
        student.mock_attitude = self.attitude
        student.mock_quality_of_resume = self.quality_of_resume
        student.mock_friendliness = self.friendliness

        self.write({'state': 'confirmed'})

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = 'Mock interview for ' + rec.student_name.name

