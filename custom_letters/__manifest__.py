# -*- coding: utf-8 -*-
{
    'name': "Letters",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
        custom letters is a custommodule for letters organizing 
    """,
    'author': "WAY_FOR_IST_Eng_Mahmoud_Rafat",
    'website': "http://www.yourcompany.com",
    'category': 'Services',
    'version': '0.1',
    'sequence': 1,
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/letters_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}