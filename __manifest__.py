# -*- coding: utf-8 -*-
{
    'name': "latihan_dimas",

    'summary': """
        Untuk membuat sistem kelas""",

    'description': """
        Untuk membuat sistem kelas
    """,

    'author': "dimas",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/kelas_views.xml',
        'views/mata_kuliah.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
