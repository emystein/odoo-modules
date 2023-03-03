{
    'name': 'Incomplete Purchase Orders',
    'category': 'Inventory/Inventory',
    'version': '1.0',
    'description': """
    Adds a filter for Purchase Order Lines 'Received quantity is less than requested'
    """,
    'depends': ['purchase', 'stock', 'basic_purchase_order_line_views'],
    'data': [
        'views/purchase_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OPL-1'
}