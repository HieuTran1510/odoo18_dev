from odoo import models, fields  # pyright: ignore[reportMissingImports]

class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    x_analytic_account_ids = fields.Many2many(
        'account.analytic.account',
        'hr_contract_analytic_rel',
        'contract_id',
        'analytic_account_id',
        string='Analytic Accounts',
        check_company=True,
        help='List of analytic accounts linked to this contract.'
    )
