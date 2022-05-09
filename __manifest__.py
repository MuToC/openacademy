# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "55",
    'website': "",

    # Categories can be used to filter modules in modules listing m2
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '1.0',

    # any module necessary for this one to work correctly
    # 'depends': ['base', 'web_gantt'],
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}