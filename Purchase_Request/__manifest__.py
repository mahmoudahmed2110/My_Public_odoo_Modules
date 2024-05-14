# -*- coding: utf-8 -*-

{
    'name': 'Purchase Request',
    'version': '0.1',
    'author': 'Mahmoud Rafat',
    'sequence': 0,
    'summary': 'YDS purchase request',
    'description':
        """
YDS purchase request===============================================

This module provides a propper  for Odoo's new models.
        """,
    'depends': [
        'purchase',
    ],
    'data': [
        'views/purchase_request_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
