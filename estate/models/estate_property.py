from odoo import fields, models 

class EstateProperty(models.Model):
   _name = 'estate.property'
   _description = 'Estate Property'
   
   name = fields.Char('Name', required=True, help="The name of the property")
   description = fields.Text('Description', help="The description of the property")
   postcode = fields.Char('Postcode', help="The postcode of the property")
   date_availability = fields.Date('Date Availability', help="The date availability of the property")
   expected_price = fields.Float('Expected Price', required=True, help="The expected price of the property")
   selling_price = fields.Float('Selling Price', help="The selling price of the property")
   bedrooms = fields.Integer('Bedrooms', help="The number of bedrooms of the property")
   living_area = fields.Integer('Living Area', help="The living area of the property")
   facades = fields.Integer('Facades', help="The number of facades of the property")
   garage = fields.Boolean('Garage', help="Whether the property has a garage or not")
   garden = fields.Boolean('Garden', help="Whether the property has a garden or not")
   garden_area = fields.Integer('Garden Area', help="The garden area of the property")
   garden_orientation = fields.Selection(
       string = 'Garden Orientation',
       selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
       help = "The direction of the garden"
   )
   