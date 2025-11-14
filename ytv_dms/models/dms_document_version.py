from odoo import models, fields

class DmsDocumentVersion(models.Model):
    _name = 'dms.document.version'
    _description = 'Phiên bản tài liệu'
    _rec_name = 'x_version_code' # hiển thị tên bản ghi ở phần header

    x_document_id = fields.Many2one('dms.document', string="Tài liệu gốc")
    x_version_code = fields.Char("Bản", required=True)
    x_author = fields.Char("Biên soạn", required=True)
    x_verifier = fields.Char("Chuẩn hoá", required=True)
    x_reviewer = fields.Char("Soát xét", required=True)
    x_approver = fields.Char("Phê duyệt", required=True)
    x_issue_date = fields.Date("Ngày ban hành", required=True)
    x_effective_date = fields.Date("Ngày hiệu lực", required=True)
    x_change_content = fields.Char("Nội dung thay đổi")

    # x_version_count = fields.Integer("Số lượng", default=1)