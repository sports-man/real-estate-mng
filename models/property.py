from odoo import models, fields

class Property(models.Model):
    _name = 'property'
    _description = 'Propiedad'

    property_type_id = fields.Many2one('property.type', string='Tipo de Propiedad')
    name = fields.Char(string='Nombre de la Propiedad')
    description = fields.Text(string='Descripción de la Propiedad')
    address_id = fields.Many2one('property.address', string='Dirección de la Propiedad')
    price = fields.Float(string='Precio de la Propiedad')
    num_bedrooms = fields.Integer(string='Número de Habitaciones')
    num_bathrooms = fields.Integer(string='Número de Baños')
    total_area = fields.Char(string='Área Total de la Propiedad')
    availability_date = fields.Date(string='Fecha de Disponibilidad')
    partner_id = fields.Many2one('res.partner', string='Partner')
    image = fields.Binary(string='Imagen')