# -*- coding: utf-8 -*-
{
    'name': 'Darbo planas',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Darbo paskirties ir planavimo įrankis',
    'author': "Martynas Vidugiris",
    'depends': ['web','mail'],
    'data': [
        'security/ir.model.access.csv',
        "views/actions.xml",
        "views/work_view.xml",
        "views/plan_view.xml",
    ],
    'demo': [],
    'css': [],
    'sequence': 1,
    'installable': True,
    'auto_install': True,
    'application': True,
}
