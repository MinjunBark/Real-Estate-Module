from odoo import fields, models 
from datetime import datetime, timedelta

class EstateProperty(models.Model):
   _name = 'estate.property'
   _description = 'Estate Property'
   
   name = fields.Char(
       string='Title',
       required=True,
       help="The name of the property"
    )
   description = fields.Text(
       string='Description',
       help="The description of the property"
    )
   postcode = fields.Char(
       string='Postcode',
       help="The postcode of the property"
    )
   date_availability = fields.Date(
       string='Date Availability', 
       copy=False,
       default=lambda self: datetime.today() + timedelta(days=90), 
       help="The date availability of the property"
    )
   expected_price = fields.Float(
       string='Expected Price',
       required=True,
       help="The expected price of the property"
    )
   selling_price = fields.Float(
       string='Selling Price', 
       copy=False,
       readonly=True, 
       help="The selling price of the property"
    )
   bedrooms = fields.Integer(
       string='Bedrooms',
       default=2,
       help="The number of bedrooms of the property"
    )
   active = fields.Boolean(
       string='Active', 
       default=True, 
       help="The active field allows you to hide the property without removing it."
    )
   state = fields.Selection(
       string='State',
       selection=[
           ('new', 'New'),
           ('offer_received', 'Offer Received'),
           ('sold', 'Sold'),
           ('cancelled', 'Cancelled')
        ],
       required=True,
       copy=False,
       default='new',
       help="The state of the property"
    )
   living_area = fields.Integer(
       string='Living Area (sqm)',
       help="The living area of the property"
    )
   facades = fields.Integer(
       string='Facades',
       help="The number of facades of the property"
    )
   garage = fields.Boolean(
       string='Garage',
       help="Whether the property has a garage or not"
    )
   garden = fields.Boolean(
       string='Garden',
       help="Whether the property has a garden or not"
    )
   garden_area = fields.Integer(
       string='Garden Area',
       help="The garden area of the property"
    )
   garden_orientation = fields.Selection(
       string = 'Garden Orientation',
       selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
       help = "The direction of the garden"
   )
   
   property_type_id = fields.Many2one(
       string='Property Type',
       comodel_name='estate.property.type',
       help="The type of the property"
    )
   buyer_id = fields.Many2one(
        string='Buyer',
        comodel_name='res.partner',
        copy=False,
        help="The buyer of the property"
    )
   salesperson_id = fields.Many2one(
        string='Salesperson',
        comodel_name='res.users',
        default=lambda self: self.env.user,
        help="The salesperson of the property"
    )
   tags_ids = fields.Many2many(
       string='Tags',
       comodel_name='estate.property.tag',
       help="The tags of the property"
    )