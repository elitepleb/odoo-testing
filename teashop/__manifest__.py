# -*- coding: utf-8 -*-
{
    'name': 'Arbatinė',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Arbatinės inventorius ir pirkimai',
    'author': "Martynas Vidugiris",
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/tea_view.xml',
        'views/customer_view.xml',
        'views/order_view.xml',
    ],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': True,
    'application': True,
}
