from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Kelas(models.Model):
    _name = 'kelas.kelas'

    name = fields.Char(string='Name')
    
    partner_id = fields.One2many(
        comodel_name='res.partner', 
        inverse_name='kelas_id', 
        string='partner id')
    

    wali_kelas = fields.Many2one(
        comodel_name='res.partner',
        domain=[
            ("is_dosen", "=", True),
        ],
        string='Wali Kelas',
    )

    matkuls = fields.Many2many(
        comodel_name='mata.kuliah', 
        string='Mata Kuliah'
    )
    

    

    
    
    

    