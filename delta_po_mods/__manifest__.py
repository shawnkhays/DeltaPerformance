# -*- coding: utf-8 -*-
{
    'name': "delta_po_mods",

    'summary': """
        Modification of Purchase Order""",

    'description': """
        Adding Purchase Terms, Freight Terms (incoterms), and remove time on Date Formats
    """,

    'author': "Talus ERP - Jeff Rund",
    'website': "http://www.taluserp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_purchaseorder_inherit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
