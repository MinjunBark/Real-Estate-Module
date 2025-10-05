from odoo import fields, models 

class EstateProperty(models.Model):
   _name = 'estate.property'
   _description = 'Estate Property'
   
   name = fields.Char(string = "Name", required = True)