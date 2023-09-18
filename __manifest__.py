{
    'name': "Mock Interview",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'mail'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/mock_interview.xml',
        'views/interviewer.xml',
        'views/interview_web_form.xml',
        'views/link_wizard.xml',
        # 'security/record_rule.xml',
        # 'views/one_to_one.xml'

    ],
    'demo': [],
    'summary': "logic_mock_interview",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}
