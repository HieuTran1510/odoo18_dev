from odoo import models, fields, api

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    x_owner_company_id = fields.Many2one(
        'res.company',
        string='Công ty sở hữu',
        help='Company that owns this sales team'
    )
    
    x_shared_company_ids = fields.Many2many(
        'res.company',
        'crm_team_shared_company_rel',
        'team_id',
        'company_id',
        string='Công ty chia sẻ',
        help='Companies that can access this sales team'
    )

