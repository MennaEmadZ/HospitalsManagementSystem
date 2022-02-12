from odoo import models, fields


class LogHistory(models.Model):
    _name = 'hms.log'
    _rec_name = 'description'

    created_by = fields.Char()
    date = fields.Date()
    description = fields.Char()
    patient_id = fields.Many2one('hms.patient')