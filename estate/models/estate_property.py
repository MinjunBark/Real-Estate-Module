from odoo import fields, models 

class EstateProperty(models.Model):
   _name = 'estate.property'
   _description = 'Estate Property'
   
   name = fields.Char(
       'Name',
       required=True,
       help="The name of the property"
    )
   description = fields.Text(
       'Description',
       help="The description of the property"
    )
   postcode = fields.Char(
       'Postcode',
       help="The postcode of the property"
    )
   date_availability = fields.Date(
       'Date Availability', 
       copy=False,
       default=lambda self: datetime.today() + timedelta(days=90), 
       help="The date availability of the property"
    )
   expected_price = fields.Float(
       'Expected Price',
       required=True,
       help="The expected price of the property"
    )
   selling_price = fields.Float(
       'Selling Price', 
       copy=False,
       readonly=True, 
       help="The selling price of the property"
    )
   bedrooms = fields.Integer(
       'Bedrooms',
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
       'Living Area',
       help="The living area of the property"
    )
   facades = fields.Integer(
       'Facades',
       help="The number of facades of the property"
    )
   garage = fields.Boolean(
       'Garage',
       help="Whether the property has a garage or not"
    )
   garden = fields.Boolean(
       'Garden',
       help="Whether the property has a garden or not"
    )
   garden_area = fields.Integer(
       'Garden Area',
       help="The garden area of the property"
    )
   garden_orientation = fields.Selection(
       string = 'Garden Orientation',
       selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
       help = "The direction of the garden"
   )
   