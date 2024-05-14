# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Product Button',
    'auther': 'Mahmoud',
    'sequence': 11,
    'installable': True,
    'license': 'LGPL-3',
    'demo': [],
    'depends': ['base', 'web'],
    'data': [
    ],
    'assets':{
        'web.assets_backend':[
            "wb_product_button/static/src/xml/list_controller.xml",
            "wb_product_button/static/src/js/list_controller.js"
        ],
    },
    'application': True,
    'auto_install': False,
}
