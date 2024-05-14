# -*- coding: utf-8 -*-

{

    "name": "Strategized Penalities",
    "summary": "Penality MOdule to create  employees penalities",
    "author": "Mahmoud-Rafat" "stratizied Company" "Odoo Enterprize Association (OCA)",
    "website": "",
    "category": "Accounting",
    "version": "15.0.1.1.4",
    "development_status": "Mature",
    "license": "AGPL-3",
    'sequence': 3,
    "depends": ["base","hr","hr_payroll"],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/penalities_views.xml',
        'views/hr_employee_view_inherit.xml',
        'views/hr_payslib_view_inherit.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
