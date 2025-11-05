{
    'name': 'YTV Product Sharing Multi-Company',
    'summary': 'Phân quyền đối tác đa công ty',
    'author': 'Ban QTHT_YTV',
    'version': '18.0.1.0.0',
    'depends': ['product'],
    'data': [
       'security/product_rule.xml',
        'views/product_views.xml',
        'views/res_users_views.xml',
        'views/product_category_views.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}