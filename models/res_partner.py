from odoo import api, fields, models
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # age = fields.Integer(string='Age')

    age_days = fields.Integer( 
        string='Umur', 
        compute='_compute_age', 
        inverse='_inverse_age', 
        search='_search_age', 
        store=False, # optional
        compute_sudo=True, # optional 
        readonly=True,
    )

    @api.depends('tanggal_lahir')
    def _compute_age(self):
        today = fields.Date.today()
        for book in self:
            if book.tanggal_lahir:
                delta = today - book.tanggal_lahir
                book.age_days = int(delta.days/365)
            else:
                book.age_days = 0
    
    @api.constrains('tanggal_lahir')
    def _check_tanggal(self): 
        tanggal_lahir = self.tanggal_lahir
        if tanggal_lahir and tanggal_lahir > fields.Date.today(): 
            raise models.ValidationError( 'Error! tanggal lahir tidak valid.')


    kelas_id = fields.Many2one(
        comodel_name='kelas.kelas',
        string="Kelas ID",
        # related="partner_id.company_id",
    )

    tanggal_lahir = fields.Date('Tanggal Lahir') 

    is_dosen = fields.Boolean(string='Dosen')



    