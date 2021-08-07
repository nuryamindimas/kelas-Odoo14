from odoo import models, fields, api

class MataKuliah(models.Model):
    _name = 'mata.kuliah'

    name = fields.Char(string='Nama mata kuliah')
    kode = fields.Char(string='kode matakuliah')
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Dosen Pengampu",
        domain=[
            ("is_dosen", "=", True),
        ],
        # related="partner_id.company_id",
    )
    
    kelas_ids = fields.Many2many(
        comodel_name='kelas.kelas', 
        string='Kelas'
    )
    

    

    