# -*- coding: utf-8 -*-
{
    'name': 'University Application',
    'version': '1.0.0.0',
    'category': 'Education/Order',
    'summary': """University Application System is custom addon for 
                 students applications management of university""",
    'sequence': 3,
    'license': 'AGPL-3',
    'author': 'Eng Mahmoud Raafat',
    'maintainer': 'Eng Mahmoud Raafat',
    'website': 'www.universitywebsite.com',
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/university_application_request.xml',
        'views/university_studentrelatives.xml',
        'views/university_faculty.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
