from odoo import models, fields

class DmsDocument(models.Model):
    _name = 'dms.document'
    _description = 'Danh mục tài liệu'
    _rec_name = 'x_name' # hiển thị tên bản ghi ở phần header

    # code = fields.Char("Mã tài liệu", required=True)
    x_name = fields.Char("Tên tài liệu", required=True)
    x_description = fields.Char("Mô tả")
    x_link = fields.Char("Link tài liệu", required=True)

    x_version_ids = fields.One2many('dms.document.version', 'x_document_id', string="Phiên bản")