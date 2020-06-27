# -*- coding: utf-8 -*-
{
    'name': 'BOL Report',
    'category': 'Inventory',
    'description': """
New Report
=============================
""",
    'version': '1.0',
    'depends': [
        'stock',
        'sale',
        'account',
    ],
    'data': [
        'views/view.xml',
        'views/report.xml',
        'views/bol_report.xml',
    ],
    'installable': True,
}
