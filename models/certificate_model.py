from datetime import date
from odoo.tools.translate import _
from odoo import models, fields, api

cnt=0
list1=[]
year_now=int(date.today().year)
for i in range(year_now-20,year_now+1):
         list1.append((str(cnt),str(i)))
         cnt=cnt+1
class Certificate(models.Model):
    _name = 'certificate_system.certificate'
    vehicle_type=fields.Selection([('1', 'Car'), ('2', 'Bus'), ('3', 'Minibus'), ('4', 'Microbus')], string="vehicle type", required=True)
    certificate_type = fields.Many2one('certificate_system.certificate_type',required=True)
    traffic_department = fields.Many2one('certificate_system.traffic_department',required=True)
    vehicle_model = fields.Selection(list1, string='vehicle model', required=True, copy=True)
    brand=fields.Many2one('certificate_system.brand',required=True)
    customer=fields.Many2one('res.partner',required=True)
    price=fields.Float(required=True)
    serial_number = fields.Char(string='Serial Number', required=True,
                          readonly=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('serial_number', _('New')) == _('New'):
            vals['serial_number'] = self.env['ir.sequence'].next_by_code(
                'certificate_system.certificate') or _('New')
        res = super(Certificate, self).create(vals)
        return res

