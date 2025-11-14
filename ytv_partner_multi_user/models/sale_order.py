from odoo import models, api, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Giới hạn dropdown salesperson theo x_user_ids
    user_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        domain=lambda self: self._domain_salesperson()
    )

    def _domain_salesperson(self):
        """Domain: nếu partner có x_user_ids → chỉ hiển thị user đó."""
        partner = self.partner_id
        if partner and partner.x_user_ids:
            return [('id', 'in', partner.x_user_ids.ids)]
        return []  # Hiển thị toàn bộ user nếu không có multi-user

    @api.onchange('partner_id')
    def _onchange_partner_id_assign_salesperson(self):
        """Assign user_id theo thứ tự ưu tiên:
           1. x_user_ids
           2. partner.user_id
           3. user đang đăng nhập
        """
        partner = self.partner_id

        if partner:
            # 1. Ưu tiên x_user_ids
            if partner.x_user_ids:
                self.user_id = partner.x_user_ids[0].id

            # 2. Nếu không có x_user_ids → dùng user_id gốc
            elif partner.user_id:
                self.user_id = partner.user_id.id

            # 3. Cuối cùng → user đăng nhập
            else:
                self.user_id = self.env.user.id
        else:
            self.user_id = False

    @api.model
    def create(self, vals):
        """Assign user_id tự động khi tạo qua API/import."""
        if vals.get('partner_id') and not vals.get('user_id'):
            partner = self.env['res.partner'].browse(vals['partner_id'])

            # 1. Nếu có x_user_ids
            if partner.x_user_ids:
                vals['user_id'] = partner.x_user_ids[0].id

            # 2. Nếu không có x_user_ids nhưng có user_id gốc
            elif partner.user_id:
                vals['user_id'] = partner.user_id.id

            # 3. Cuối cùng → user đăng nhập
            else:
                vals['user_id'] = self.env.uid

        return super().create(vals)
