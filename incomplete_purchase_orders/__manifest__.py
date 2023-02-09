{
    'name': 'Incomplete Purchase Orders',
    'category': 'Inventory/Inventory',
    'version': '1.0',
    'depends': ['purchase', 'stock', 'basic_purchase_order_line_views'],
    'data': [
        'views/purchase_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1'
}