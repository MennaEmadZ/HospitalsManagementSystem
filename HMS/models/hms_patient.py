from odoo.exceptions import UserError
from odoo import models, fields, api
from datetime import date
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class Patient(models.Model):
    _name = 'hms.patient'
    _rec_name = 'first_name'
    # _log_access = False b
    first_name = fields.Char()
    last_name = fields.Char()
    birth_date = fields.Date()
    age = fields.Integer()
    address = fields.Text()
    PCR = fields.Boolean()
    CR_ratio = fields.Float()
    image = fields.Image()
    blood_types = fields.Selection([ ('a+','A+'),
                                     ('a-','A+'),
                                     ('b+','B+'),
                                     ('b-','B+'),
                                     ('ab+','AB+'),
                                     ('ab-','AB+'),
                                     ('o+','O+'),
                                     ('o-','O+'),])
    history = fields.Html()
    dept_id = fields.Many2one('hms.dept')
    capacity = fields.Integer(related='dept_id.capacity')

    doc_id = fields.Many2many('hms.doc')

    # log_id = fields.Many2many('hms.log')

    log_ids = fields.One2many('hms.log','patient_id')

    cust_id = fields.Many2one('res.partner','related_patient_id')

    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined')

    email = fields.Char()

    @api.constrains('email')
    def _check_email_validation(self):
        if not re.fullmatch(regex, self.email):
            raise UserError("Invalid Email.")

    @api.onchange('age')
    def _onchange_age(self):
        if self.age<30:
            self.PCR= True
            return {
                'warning': {
                    'title': 'PCR Changed',
                    'message': 'PCR has been Checked.'
                }
            }


    def create_log_history(self):
        log = self.env['hms.log'].create({
            'patient_id': self.id,
            'created_by': self.first_name,
            'date': date.today(),
            'description': self.state
        })

    def onchange_state(self):
        self.create_log_history()
        return {
            'warning': {
                'title': 'Log History',
                'message': 'Log History has been added.'
            }
        }

    @api.onchange('birth_date')
    def _onchange_birth_date(self):
        if self.birth_date:
            self.age = date.today().year - self.birth_date.year

    def undetermined(self):
        self.state = 'undetermined'
        self.onchange_state()
    def good(self):
        self.state = 'good'
        self.onchange_state()
    def fair(self):
        self.state = 'fair'
        self.onchange_state()
    def serious(self):
        self.state = 'serious'
        self.onchange_state()
