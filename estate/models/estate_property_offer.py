from odoo import api,fields, models 
from datetime import datetime, timedelta

class EstatePropertyType(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'
    
    price = fields.Float(
        string='Price',
    )
    status = fields.Selection(
        string="Status",
        selection =[('accepted', 'Accepted'), ('refused', 'Refused')],
        copy = False
    )
    partner_id = fields.Many2one(
        string='Partner',
        comodel_name='res.partner',
        required = True
    )
    property_id = fields.Many2one(
        string='Property',
        comodel_name='estate.property',
        required = True
    )
    # ----CHAPTER 9----
    validity = fields.Integer(
        string='Validity',
        default=7
    )
    date_deadline = fields.Date(
        string='Deadline',
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline'
    )
            
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            base_date = record.create_date or fields.Date.today()
            record.date_deadline = base_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                base_date = record.create_date or fields.Date.today()
                delta = (record.date_deadline - base_date).days
                record.validity = max(delta, 0)  # Ensure non-negative validity
            else:
                record.validity = 0