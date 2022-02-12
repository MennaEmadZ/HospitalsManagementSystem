from odoo import models, fields


class Department(models.Model):
    _name = 'hms.dept'

    # _log_access = False b
    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patient_ids = fields.One2many('hms.patient', 'dept_id')