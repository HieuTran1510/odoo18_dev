from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # 1
    x_ytv_registration_no = fields.Char(
        string='Số lưu hành (VN)',
        help='Số lưu hành sản phẩm'
    )
    # 2
    x_ytv_registration_certificate_vn = fields.Char(
        string='GCN ĐKLH (VN)',
        help='Link giấy chứng nhận đăng ký lưu hành thiết bị y tế tại Việt Nam'
    )
    # 3
    x_ytv_medical_equipment_classification = fields.Char(
        string='Phân loại TBYT',
        help='Link bản kết quả phân loại thiết bị y tế'
    )
    # 4
    x_ytv_product_owner_authorization = fields.Char(
        string='UQ CSH',
        help='Link giấy ủy quyền của chủ sở hữu thiết bị y tế'
    )
    # 5
    x_ytv_eligibility_warranty = fields.Char(
        string='XN BH TBYT',
        help='Link giấy xác nhận đủ điều kiện bảo hành'
    )
    # 6
    x_ytv_single_use_medical_declaration = fields.Char(
        string='XN TBYT SD 1 lần',
        help='Link văn bản xác nhận thiết bị y tế sử dụng 1 lần'
    )
    # 7
    x_ytv_product_standard_vn = fields.Char(
        string='TCSP (VN)',
        help='Link tiêu chuẩn sản phẩm (tiếng Việt)'
    )
    # 8
    x_ytv_product_standard_en = fields.Char(
        string='TCSP (EN)',
        help='Link tiêu chuẩn sản phẩm (tiếng Anh)'
    )
    # 9
    x_ytv_iso_13485_cert = fields.Char(
        string='ISO 13485',
        help='Link ISO 13485'
    )
    # 10
    x_ytv_mdsap_cert = fields.Char(
        string='MDSAP',
        help='Link MDSAP'
    )
    # 11
    x_ytv_production_country_license = fields.Char(
        string='GPLH nước SX',
        help='Link giấy phép lưu hành thiết bị y tế tại nước sản xuất'
    )
    # 12
    x_ytv_fsc_cert_origin = fields.Char(
        string='FSC nước SX',
        help='Link FSC tại nước sản xuất'
    )
    # 13
    x_ytv_fsc_cert_eu = fields.Char(
        string='EU FSC',
        help='Link EU FSC'
    )
    # 14
    x_ytv_doc_ce_cert = fields.Char(
        string='DOC/CE',
        help='Link DOC/CE'
    )
    # 15
    x_ytv_us_cfg_cert = fields.Char(
        string='US CFG',
        help='Link US CFG'
    )
    # 16
    x_ytv_us_fda_801_cert = fields.Char(
        string='US FDA 801',
        help='Link US FDA 801'
    )
    # 17
    x_ytv_us_fda_802_cert = fields.Char(
        string='US FDA 802',
        help='Link US FDA 802'
    )
    # 18
    x_ytv_testing_certificate_vn = fields.Char(
        string='GCN kiểm định (VN)',
        help='Link giấy chứng nhận kiểm định (tiếng Việt)'
    )
    # 19
    x_ytv_external_test_result_vn = fields.Char(
        string='KQ ngoại kiểm (VN)',
        help='Link kết quả ngoại kiểm (tiếng Việt)'
    )
    # 20
    x_ytv_external_test_result_en = fields.Char(
        string='KQ ngoại kiểm (EN)',
        help='Link kết quả ngoại kiểm (tiếng Anh)'
    )
    # 21
    x_ytv_ilac_cert = fields.Char(
        string='ILAC',
        help='Link ILAC'
    )
    # 22
    x_ytv_iaf_cert = fields.Char(
        string='IAF',
        help='Link IAF'
    )
    # 23
    x_ytv_packaging_label_sample = fields.Char(
        string='Bao bì, mẫu nhãn',
        help='Link bao bì, mẫu nhãn'
    )
    # 24
    x_ytv_user_manual_vn = fields.Char(
        string='HDSD (VN)',
        help='Link hướng dẫn sử dụng (tiếng Việt)'
    )
    # 25
    x_ytv_user_manual_en = fields.Char(
        string='HDSD (EN)',
        help='Link hướng dẫn sử dụng (tiếng Anh)'
    )
    # 26
    x_ytv_msds_doc = fields.Char(
        string='MSDS',
        help='Link MSDS'
    )
    # 27
    x_ytv_coa_sample = fields.Char(
        string='Mẫu COA',
        help='Link mẫu COA'
    )
    # 28
    x_ytv_preclinical_report = fields.Char(
        string='Báo cáo tiền lâm sàng',
        help='Link báo cáo nghiên cứu tiền lâm sàng'
    )
    # 29
    x_ytv_clinical_report = fields.Char(
        string='Báo cáo lâm sàng',
        help='Link báo cáo nghiên cứu lâm sàng'
    )
    # 30
    x_ytv_explanation = fields.Char(
        string='Giải trình',
        help='Link công văn giải trình có liên quan đến sản phẩm'
    )
    # 31
    x_ytv_sales_docs_folder_vn = fields.Char(
        string='Thư mục TLBH (VN)',
        help='Link thư mục tài liệu bán hàng (tiếng Việt)'
    )
    # 32
    x_ytv_sales_docs_folder_en = fields.Char(
        string='Thư mục TLBH (EN)',
        help='Link thư mục tài liệu bán hàng (tiếng Anh)'
    )
    # 33
    x_ytv_coa_folder = fields.Char(
        string='Thư mục COA',
        help='Link thư mục COA'
    )
    # 34
    x_ytv_catalog_en = fields.Char(
        string='Catalog EN',
        help='Link catalog (tiếng Anh)'
    )
    # 35
    x_ytv_catalog_vn = fields.Char(
        string='Catalog VN',
        help='Link catalog (tiếng Việt)'
    )
