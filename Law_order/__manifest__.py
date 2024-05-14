# -*- coding: utf-8 -*-

{
    'name': 'Law Order',
    'version': '1.1',
    'category': 'Law/Order',
    'sequence': 1,
    'summary': 'Centralize law   order information',
    'description': "",
    # 'website': 'https://www.odoo.com/page/employees',
    'images': [
        # 'images/hr_department.jpeg',
        # 'images/hr_employee.jpeg',
        # 'images/hr_job_position.jpeg',
        # 'static/src/img/default_image.png',
    ],
    'depends': [
        'base',
        'sale',
        # 'base_setup',
        # 'mail',
        # 'resource',
        # 'web',
        # 'mail_bot',
    ],
    'data': [
        'views/lawyers_views.xml',
        'views/customers_views.xml',
        'views/inherit_sales.xml',
        'security/ir.model.access.csv',
        # # 'security/hr_security.xml',
        # 'security/ir.model.access.csv',
        # 'wizard/hr_plan_wizard_views.xml',
        # 'wizard/hr_departure_wizard_views.xml',
    ],
    'demo': [
        # 'data/hr_demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'qweb': ['static/src/xml/hr_templates.xml'],
    'license': 'LGPL-3',
}
