from odoo import api,fields, models 
from datetime import datetime, timedelta
from odoo.exceptions import UserError

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
        inverse='_inverse_date_deadline',
        store=False
    )
            
    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:
            base_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = base_date + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                base_date = record.create_date.date() if record.create_date else fields.Date.today()
                delta = (record.date_deadline - base_date).days
                record.validity = max(delta, 0)  # Ensure non-negative validity
            else:
                record.validity = 0
                
    def action_accept(self):
        for record in self:
            if record.property_id.offer_ids.filtered(lambda o: o.status == 'accepted' and o.id != record.id):
                raise UserError ("Only one offer can be accepted for a property.")
            record.status='accepted'
            record.property_id.write(({
                'buyer_id': record.partner_id.id,
                'selling_price': record.price,
                'state': 'offer_received' if record.property_id.state not in ('sold', 'cancelled') else record.property_id.state
            }))
        return True
    
    def action_refuse(self):
        for record in self:
            record.status = 'refused'
        return True
    
    _sql_constraints = [
        ('check_price', 'CHECK(price > 0)', 'The price must be strictly positive.')
    ]