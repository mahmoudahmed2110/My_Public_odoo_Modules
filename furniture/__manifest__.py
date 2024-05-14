# -*- coding: utf-8 -*-
{
    'name': "Furniture Management",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company_Eng_Mahmoud_Ra'afat",
    'website': "http://www.yourcompany.com",
    "license": "AGPL-3",

    'category': 'Productivity',
    'version': '0.1',
    'sequence': 2,
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/furniture_view.xml',
        'views/departments_view.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
