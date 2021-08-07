# from odoo import models, fields, api
# from odoo.exceptions import UserError

# class Kelas(models.Model):
#     _name = 'kelas.kelas'

#     name = fields.Char(string='Name')
#     partner_id = fields.One2many('res.partner', 'kelas_id', string='Partner ID')


# class ResPartner(models.Model):
#     _inherit = 'res.partner'

#     age = fields.Integer(string='Age')

#     kelas_id = fields.Many2one(
#         comodel_name='kelas.kelas',
#         string="Kelas ID",
#         # related="partner_id.company_id",
#     )
    

    