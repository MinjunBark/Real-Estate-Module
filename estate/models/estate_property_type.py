from odoo import fields, models 

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = 'sequence','name'

    name = fields.Char(
        string='Name',
        required=True
    )
    
    property_ids = fields.One2many(
        string="Properties",
        comodel_name='estate.property',
        inverse_name='property_type_id'
    )
    
    sequence = fields.Integer(
        string='Sequence',
        default=10,
        help="Used to order property types"
    )
    
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Name must be unique')
    ]