# -*- coding: utf-8 -*-
{
    'name': "Secure Unit Price",
    'version': '1.0',
    'category': 'Sale',
    'sequence': 9,
    'author': "Mahmoud_Rafat",
    'module_type': 'official',
    'summary': 'secure unit price in order lines of Sale Orders',
    'website': '',
    'images': [
        # 'static/src/img/default_image.png',
    ],
    'depends': [
        'sale',
    ],
    'data': [
        'views/secure_sale_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
