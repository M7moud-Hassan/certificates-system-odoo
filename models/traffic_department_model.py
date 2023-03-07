from odoo import models, fields


class TrafficDepartment(models.Model):
    _name = "certificate_system.traffic_department"
    name = fields.Char(string="Traffic Department", required=True)
    certificate_id = fields.One2many("certificate_system.certificate", string='certificate', inverse_name='traffic_department')