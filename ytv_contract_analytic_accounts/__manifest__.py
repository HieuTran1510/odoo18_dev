{
    'name': 'YTV Contract Analytic Accounts',
    'version': '18.0.1.0.0',
    'summary': 'Custom Many2many Analytic Accounts field to HR Contract',
    'category': 'Payroll',
    'author': 'YTV-QTHT-Huy',
    'depends': ['hr_payroll_account'],
    'data': [
        'views/hr_contract_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}