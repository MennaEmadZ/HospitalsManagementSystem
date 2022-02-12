from odoo import models, fields, api
from odoo.exceptions import UserError

class CustomerInhert(models.Model):
    _inherit = 'res.partner'
    # _name = 'new.model'

    # related_patient_id = fields.One2many('hms.patient','cust_id')
    related_patient_id = fields.One2many('hms.patient','cust_id')

    @api.model
    def create(self, vals):
        super(CustomerInhert, self).create(vals)

    @api.constrains('related_patient_id')
    def _check_patient_mail(self):

        if self.email == self.related_patient_id.email:
            raise UserError("Invalid Email.")

    def unlink(self):
        if not self.related_patient_id.email == False:
            raise UserError("You can not delete a customer linked to patients")
        super(CustomerInhert, self).unlink()