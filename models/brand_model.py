from odoo import models, fields


class Brand(models.Model):
    _name = 'certificate_system.brand'
    name = fields.Char(string="brand", required=True)
    certificate_id = fields.One2many("certificate_system.certificate", string='certificate', inverse_name='brand')