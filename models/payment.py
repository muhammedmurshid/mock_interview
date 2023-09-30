from odoo import models, fields, api, _


class InterviewerPayment(models.TransientModel):
    _name = 'interviewer.payment'
    _description = 'Interviewer Payment'

    interviewer_id = fields.Many2one('mock_interviewer.table', string='Interviewer', required=True)

    from_date = fields.Date('From Date', required=True)
    to_date = fields.Date('To Date', required=True)

    @api.depends('from_date', 'to_date', 'interviewer_id')
    def _compute_between_records(self):
        records = self.env['logic.mock_interview'].search([])
        count = records.search_count(
            [('date', '>=', self.from_date), ('date', '<=', self.to_date), ('interviewer', '=', self.interviewer_id.id),
             ('state', '=', 'confirmed')])
        # print(records.search_count([('date', '>=', self.from_date), '|',('date', '<=', self.to_date),
        #                            '|',('interviewer', '!=', self.interviewer_id.id), ('state', '!=', 'done')]))

        self.interview_count = count

    interview_count = fields.Integer('Interview Count', compute='_compute_between_records', store=True)

    @api.depends('from_date', 'to_date', 'interviewer_id')
    def _compute_interview_payment(self):
        payment = self.env['mock.interviewer.rate'].search([('name', '=', self.interviewer_id.id)])
        self.amount = payment.rate * self.interview_count

    amount = fields.Float('Amount', compute='_compute_interview_payment', store=True)

    def action_create_payment(self):
        if self.amount != 0:
            self.env['payment.request'].sudo().create({
                'source_type': 'mock_interview',
                'source_user': self.create_uid.id,
                'amount': self.amount,
                'mock_interviewer_id': self.interviewer_id.id,
            })
            print('self')
            records = self.env['logic.mock_interview'].search([])
            for j in records:
                if self.from_date and self.to_date:
                    if self.from_date <= j.date <= self.to_date and j.interviewer.id == self.interviewer_id.id and j.state == 'confirmed':
                        print('j', j.state)
                        j.state = 'done'


class PaymentModelInterview(models.Model):
    _inherit = 'payment.request'

    source_type = fields.Selection(
        selection_add=[('mock_interview', 'Mock Interview')], ondelete={'mock_interview': 'cascade'},
        string="Source Type",
    )
    mock_interviewer_id = fields.Many2one('mock_interviewer.table', string="Interviewer")
