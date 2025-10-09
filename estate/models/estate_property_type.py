from odoo import fields, models 

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    
    name = fields.Char(
        string='Estate Property Type',
        required=True,
        help="The name of the estate property type"
    )
    
    