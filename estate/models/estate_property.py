from odoo import fields, models 

class EstateProperty(models.Model):
   _name = 'estate.property'
   _description = 'Estate Property'
   
   
   name = fields.Char('Name', required=True, translate=True)
   description  = fields.Text('Description', required=True)
   postcode = fields.Char('Postcode', required=True)
   date_availability = fields.Date('Date Availability', required=True)
   expected_price = fields.Float('Expected Price', required=True)
   selling_price = fields.Float('Selling Price', required=True)
   bedrooms = fields.Integer('Bedrooms', required=True)
   living_area = fields.Integer('Living Area', required=True)
   facades = fields.Integer('Facades', required=True)
   garage = fields.Boolean('Garage', required=True)
   garden = fields.Boolean('Garden', required=True)
   garden_area = fields.Integer('Garden Area', required=True)
   garden_orientation = fields.Selection(
       string = 'Garden Orientation',
       selection = [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
       help = "The direction of the garden"
   )