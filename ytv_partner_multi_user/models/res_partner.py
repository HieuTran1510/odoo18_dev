from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_user_ids = fields.Many2many(
        'res.users',
        string="Chuyên viên sales",
        help="Danh sách các user phụ trách khách hàng này"
    )
