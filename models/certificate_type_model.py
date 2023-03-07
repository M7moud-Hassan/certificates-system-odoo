from odoo import models, fields


class CertificateType(models.Model):
    _name = "certificate_system.certificate_type"
    name = fields.Char(string="Certificate Type", required=True)
    certificate_id = fields.One2many("certificate_system.certificate", string='certificate', inverse_name='certificate_type')

