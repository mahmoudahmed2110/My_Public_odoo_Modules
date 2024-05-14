# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'pos webtutorials',
    'auther': 'Mahmoud',
    'depends': ['base','point_of_sale'],
    'sequence': 10,
    'installable': True,
    'license': 'LGPL-3',
    'demo': [],
    'data': [
            # "xml/view.xml",
    ],
    'assets':{
        # 'web.assets_backend':[
        #     "wb_pos/static/src/xml/list_controller.xml"
        # ],
        'point_of_sale.assets': [
            "wb_pos/static/src/js/wb_sample_button.js",
            "wb_pos/static/src/xml/wb_sample_button.xml",
            "wb_pos/static/src/js/clearall_button.js",
            "wb_pos/static/src/xml/clearall_button.xml",
        ]
    },
    'application': True,
    'auto_install': False,
}
