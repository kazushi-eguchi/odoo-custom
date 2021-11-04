# -*- coding: utf-8 -*-
{
    'name': "Sales Order Project",

    'summary': """        
        Create a project from a sales order.
    """,

    'description': """
        Create a project from a sales order.
    """,

    'author': "Kazushi Eguchi(EnzanTrades Inc,)",
    'website': "https://enzantrades.co.jp",
    'category': 'Services/Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sale_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
