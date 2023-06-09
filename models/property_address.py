from odoo import models, fields, api


class PropertyAddress(models.Model):
    _name = 'property.address'
    _description = 'Property Address'

    street = fields.Char(string='Street', required=True)
    street2 = fields.Char(string='Street 2')
    city = fields.Char(string='Ciudad', required=True)
    state_id = fields.Many2one('res.country.state', string='Provincia', required=True)
    country_id = fields.Many2one('res.country', string='País', required=True)
    zip = fields.Char(string='Código Postal')
    neighborhood = fields.Char(string='Sector', required=True)
    building = fields.Char(string='Edificio')
    floor = fields.Char(string='Piso')
    apartment = fields.Char(string='Apartamento')
    name = fields.Char(string='Nombre', store=True)

    @api.model
    def create(self, vals):
        # The `name` field is a computed field that concatenates the values of the
        # `zip`, `country_id`, `state_id`, `street`, and `neighborhood` fields.
        name = ''
        if vals.get('zip'):
            name += vals['zip']
        if vals.get('country_id'):
            country = self.env['res.country'].browse(vals['country_id'])
            name += ' - ' + country.name
        if vals.get('state_id'):
            state = self.env['res.country.state'].browse(vals['state_id'])
            name += ', ' + state.name
        if vals.get('street'):
            name += ', ' + vals['street']
        if vals.get('neighborhood'):
            name += ', ' + vals['neighborhood']
        vals['name'] = name
        return super(PropertyAddress, self).create(vals)
