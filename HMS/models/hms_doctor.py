from odoo import models, fields


class Doctor(models.Model):
    _name = 'hms.doc'
    _rec_name = 'first_name'
    # _log_access = False b
    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Image()