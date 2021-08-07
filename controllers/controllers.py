# -*- coding: utf-8 -*-
# from odoo import http


# class LatihanDimas(http.Controller):
#     @http.route('/latihan_dimas/latihan_dimas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan_dimas/latihan_dimas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('latihan_dimas.listing', {
#             'root': '/latihan_dimas/latihan_dimas',
#             'objects': http.request.env['latihan_dimas.latihan_dimas'].search([]),
#         })

#     @http.route('/latihan_dimas/latihan_dimas/objects/<model("latihan_dimas.latihan_dimas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('latihan_dimas.object', {
#             'object': obj
#         })
