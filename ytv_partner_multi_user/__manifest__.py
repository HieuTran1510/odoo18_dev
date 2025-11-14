# -*- coding: utf-8 -*-
{
    'name': 'YTV Partner Multi-User',
    'version': '18.0.1.0.0',
    'summary': 'Phân quyền nhiều chuyên viên sale cho cùng một đối tác',
    'author': 'Ban QTHT-YTV',
    'depends': ['base', 'sale_management'],
    'data': [
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}
