# -*- coding: utf-8 -*-
{
    'name': "Bienes Raíces",

    'summary': """
        Este es un módulo personalizado de inmobiliaria para gestionar inmuebles y sus detalles.
        Incluye modelos para tipos de propiedad y propiedades, así como vistas correspondientes.
    """,

    'description': """
        Módulo personalizado de inmobiliaria para gestionar inmuebles y sus detalles.
    """,

    'author': "Frainer Encarnación",
    'website': "https://github.com/fraineralex",

    'category': 'Real Estate',
    'version': '0.1',
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