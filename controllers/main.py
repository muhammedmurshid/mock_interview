from odoo import http
from odoo.http import request
import base64


class WebStudentFeedbackForm(http.Controller):
    @http.route(['/mock_interview/<string:user_id>'], type='http', auth="public", website=True)
    def feedback(self, user_id, **kw):
        decoded_bytes = base64.b64decode(user_id)
        user_id = int.from_bytes(decoded_bytes, byteorder='big')
        user = request.env['interview.attend.students.list'].sudo().browse(user_id)
        values = {
            'coord_id': user.coordinator_id.id,
            'coordinator': user.coordinator_id.name,
            'user': user.interviewer_id.id,
            'name': user.interviewer_id.name,
            'students': user.students_list_ids,
        }
        print("feedback")
        return request.render("mock_interview.mock_interview_web_form_template", values)

    @http.route(['/mock_interview/submit'], type='http', auth="public", website=True, csrf=False)
    def create_data_feedback(self, **kw):
        print("create_data_feedback")
        communication = int(kw.get('communication', 0))
        language = int(kw.get('language', 0))
        presentation = int(kw.get('presentation', 0))
        confidence = int(kw.get('confidence', 0))
        body = int(kw.get('body', 0))
        dressing = int(kw.get('dressing', 0))
        attitude = int(kw.get('attitude', 0))
        quality = int(kw.get('quality', 0))
        friendliness = int(kw.get('friendliness', 0))
        # print(kw.get('feedback_name'), 'feed')
        # print(kw.get('coordinator'), 'coor')
        print("student_id", kw.get('student'))
        print("interviewer_id", kw.get('custom_interviewer_id'))
        op = request.httprequest.form.getlist('student')
        print(kw, 'op')
        #
        request.env['logic.mock_interview'].sudo().create({
            'student_name': int(kw.get('student')),
            'coordinator': kw.get('coordinator'),
            'communication_skill': str(communication),
            'language_skill': str(language),
            'presentation_skill': str(presentation),
            'confidence_level': str(confidence),
            'body_language': str(body),
            'dressing_pattern': str(dressing),
            'attitude': str(attitude),
            'quality_of_resume': str(quality),
            'friendliness': str(friendliness),
            'interviewer': int(kw.get('custom_interviewer_id')),

        })

        return request.render('mock_interview.tmp_mock_interview_thanks')
        # print("create_data_feedback")
        # here in kw you can get the inputted value
