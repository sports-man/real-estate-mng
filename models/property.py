from odoo.exceptions import ValidationError
from odoo import models, fields, api

class Property(models.Model):
    _name = 'property'
    _description = 'Propiedad'

    property_type_id = fields.Many2one('property.type', string='Tipo de Propiedad', required=True)
    name = fields.Char(string='Nombre de la Propiedad', required=True)
    description = fields.Text(string='Descripción de la Propiedad', required=True)
    address_id = fields.Many2one('property.address', string='Dirección de la Propiedad', required=True)
    price = fields.Float(string='Precio de la Propiedad', required=True)
    num_bedrooms = fields.Integer(string='Número de Habitaciones')
    num_bathrooms = fields.Integer(string='Número de Baños')
    total_area = fields.Char(string='Área Total de la Propiedad', required=True)
    availability_date = fields.Date(string='Fecha de Disponibilidad', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    image = fields.Binary(string='Imagen')

    @api.constrains('price')
    def _check_price_positive(self):
    # Checks if the price of a record is positive and raises a validation error if it is not.
        for record in self:
            if record.price <= 0:
                raise ValidationError("El precio debe ser mayor que cero.")