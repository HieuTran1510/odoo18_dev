from odoo import models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id', 'company_id')
    def _onchange_partner_id_set_team(self):
        """Tự động chọn team theo công ty đang active của user."""
        partner = self.partner_id
        if not partner or not partner.team_ids:
            return
        
        # Công ty đang active của user (ưu tiên tuyệt đối)
        active_company = self.env.company
        teams = partner.team_ids

        # 1. Team owner = công ty active
        owner_team = teams.filtered(lambda t: t.x_owner_company_id == active_company)

        # 2. Team có shared với công ty active
        shared_team = teams.filtered(lambda t: active_company in t.x_shared_company_ids)

        # 3. Team có company_id = công ty active
        same_company_team = teams.filtered(lambda t: t.company_id == active_company)

        # Gộp theo thứ tự ưu tiên
        matching_team = (
            owner_team
            or shared_team
            or same_company_team
            or teams  # fallback
        )

        self.team_id = matching_team[0].id
