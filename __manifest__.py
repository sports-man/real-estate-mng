# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': """
        This is a customized real estate module to manage properties and their details.
        It includes templates for property types and properties, as well as corresponding views.
    """,

    'description': """
        Customized real estate module to manage properties and their details.
    """,

    'author': "Frainer Encarnación",
    'website': "https://github.com/fraineralex",

    'category': 'Real Estate',
    'version': '1.0',
    'depends': ['base', 'sale'],

    'data': [
        # views
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_address_view.xml',
        'views/ir.ui.menu.xml',

        # security
        'security/ir.model.access.csv',        
    ],
    'icon': 'real_estate_manager/static/src/img/icon.png',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}