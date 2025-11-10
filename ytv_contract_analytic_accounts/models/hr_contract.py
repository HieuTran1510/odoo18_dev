from odoo import models, fields


class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    analytic_account_ids = fields.Many2many(
        'account.analytic.account',
        'hr_contract_analytic_rel',
        'contract_id',
        'analytic_account_id',
        string='Analytic Accounts',
        check_company=True,
        # default=lambda self: [],
        help='List of analytic accounts linked to this contract.'
    )
