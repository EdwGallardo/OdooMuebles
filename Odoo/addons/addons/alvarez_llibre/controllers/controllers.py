# -*- coding: utf-8 -*-
# from odoo import http


# class AlvarezLlibre(http.Controller):
#     @http.route('/alvarez_llibre/alvarez_llibre', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/alvarez_llibre/alvarez_llibre/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('alvarez_llibre.listing', {
#             'root': '/alvarez_llibre/alvarez_llibre',
#             'objects': http.request.env['alvarez_llibre.alvarez_llibre'].search([]),
#         })

#     @http.route('/alvarez_llibre/alvarez_llibre/objects/<model("alvarez_llibre.alvarez_llibre"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('alvarez_llibre.object', {
#             'object': obj
#         })
