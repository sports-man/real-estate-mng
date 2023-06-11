from odoo import models, fields

class PropertyType(models.Model):
    _name = 'property.type'
    _description = 'Property Type'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description', required=True)