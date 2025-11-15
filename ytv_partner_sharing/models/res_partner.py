from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Công ty sở hữu duy nhất
    x_owner_company_id = fields.Many2one(
        'res.company',
        string='Công ty sở hữu',
        help="Công ty sở hữu đối tác này."
    )

    # Các công ty được chia sẻ
    x_shared_company_ids = fields.Many2many(
        'res.company',
        string='Công ty chia sẻ',
        help="Các công ty được phép truy cập đối tác này."
    )

@api.model
    def write(self, vals):
        res = super(ResPartner, self).write(vals)

        fields_to_sync = ['x_owner_company_id', 'x_shared_company_ids']

        # Nếu có field nào cần đồng bộ được thay đổi
        if any(f in vals for f in fields_to_sync):
            for partner in self:
                # Chỉ đồng bộ cho child records (liên hệ con)
                children = self.search([('parent_id', '=', partner.id)])

                # Đồng bộ x_owner_company_id
                if 'x_owner_company_id' in vals:
                    children.write({
                        'x_owner_company_id': vals['x_owner_company_id']
                    })

                # Đồng bộ x_shared_company_ids (Many2many)
                if 'x_shared_company_ids' in vals:
                    children.write({
                        'x_shared_company_ids': vals['x_shared_company_ids']
                    })

        return res