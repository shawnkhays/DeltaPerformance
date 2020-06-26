# -*- coding: utf-8 -*-
{
    'name': "prod_pack_dec",

    'summary': """
        Increase the Contained quantity to 3 decimals on the Product Packaging.""",

    'description': """
        Increase the Contained quantity from 2 decimals to 3 decimals on the Product Packaging in Inventory.  
    """,

    'author': "Talus ERP - Jeff A. Rund",
    'website': "http://www.taluserp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.4',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
