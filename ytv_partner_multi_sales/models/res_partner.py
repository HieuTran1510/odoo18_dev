from odoo import models, fields, api
from odoo.osv import expression

def _domain_team(model):
    """Domain để lọc Sales Team theo tất cả các công ty đang được activate"""
    active_company_ids = model.env.companies.ids
    # Domain lọc theo tất cả các công ty đang activate:
    # - Team có owner là một trong các công ty activate
    # - Team có shared với một trong các công ty activate
    # - Team có company_id là một trong các công ty activate
    # - Team global (company_id = False)
    return expression.OR([
        [('x_owner_company_id', 'in', active_company_ids)],
        [('x_shared_company_ids', 'in', active_company_ids)],
        [('company_id', 'in', active_company_ids)],
        [('company_id', '=', False)],
    ])

class ResPartner(models.Model):
    _inherit = 'res.partner'

    team_ids = fields.Many2many(
        'crm.team',
        'res_partner_crm_team_rel',
        'partner_id',
        'team_id',
        string="Bộ phận sales",
        domain=_domain_team,
    )