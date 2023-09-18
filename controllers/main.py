from odoo import http
from odoo.http import request
import base64


class WebStudentFeedbackForm(http.Controller):
    @http.route(['/mock_interview/<string:user_id>'], type='http', auth="public", website=True)
    def feedback(self, user_id, **kw):
        decoded_bytes = base64.b64decode(user_id)
        user_id = int.from_bytes(decoded_bytes, byteorder='big')
        # batch = request.env['logic.base.ba'].sudo().search([])
        user = request.env['mock_interviewer.table'].sudo().browse(user_id)
        values = {
            'id': user.id,
            'name': user.name,
        }
        print("feedback")
        return request.render("mock_interview.mock_interview_web_form_template", values)

    @http.route(['/mock_interview/submit'], type='http', auth="public", website=True, csrf=False)
    def create_data_feedback(self, **post):
        print("create_data_feedback")
        communication = int(post.get('communication', 0))
        language = int(post.get('language', 0))
        presentation = int(post.get('presentation', 0))
        confidence = int(post.get('confidence', 0))
        body = int(post.get('body', 0))
        dressing = int(post.get('dressing', 0))
        attitude = int(post.get('attitude', 0))
        quality = int(post.get('quality', 0))
        friendliness = int(post.get('friendliness', 0))
        # print(post.get('feedback_name'), 'feed')
        # print(post.get('coordinator'), 'coor')
        #
        request.env['logic.mock_interview'].sudo().create({
            'student_name': post.get('student_name'),
            'communication_skill': str(communication),
            'language_skill': str(language),
            'presentation_skill': str(presentation),
            'confidence_level': str(confidence),
            'body_language': str(body),
            'dressing_pattern': str(dressing),
            'attitude': str(attitude),
            'quality_of_resume': str(quality),
            'friendliness': str(friendliness),
            'interviewer': post.get('interviewer'),

        })
        return request.render('mock_interview.tmp_mock_interview_thanks')
        # print("create_data_feedback")
        # here in kw you can get the inputted value
