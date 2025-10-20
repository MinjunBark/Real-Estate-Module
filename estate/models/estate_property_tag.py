from odoo import fields, models 

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    _order = 'name'

    name = fields.Char(
        string='Name',
        required=True,
        store=True
    )
    
    color = fields.Integer(
        string='Color'
    )
    
    
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Tag name must be unique')
    ]