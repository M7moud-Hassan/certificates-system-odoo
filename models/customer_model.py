from odoo import models, fields

class Custommer(models.Model):
    _inherit = 'res.partner'
    certificate_id = fields.One2many("certificate_system.certificate", string='certificate',
                                     inverse_name='customer')
