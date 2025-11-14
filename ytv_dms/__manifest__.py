{
    'name': 'DMS – Quản lý danh mục tài liệu',
    'version': '18.0.1.0.0',
    'summary': 'Quản lý danh mục và phiên bản tài liệu',
    'author': 'YTV-QTHT-Huy',
    'category': 'Documents',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/dms_document_views.xml',
        'views/dms_report_views.xml',
        'views/dms_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}