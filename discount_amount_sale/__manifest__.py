# -*- coding: utf-8 -*-
{
    'name': "Discount Amount Sale App",
    'version': '1.0',
    'category': 'Sale',
    'sequence': 10,
    'author': "Mahmoud_Rafat",
    'module_type': 'official',
    'summary': 'secure unit price in order lines of Sale Orders',
    'website': '',
    'images': [
        # 'static/src/img/default_image.png',
    ],
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/discount_res_config_settings.xml',
        'views/discount_sale_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
