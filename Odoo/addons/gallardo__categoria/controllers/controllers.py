# -*- coding: utf-8 -*-
# from odoo import http


# class GallardoCategoria(http.Controller):
#     @http.route('/gallardo__categoria/gallardo__categoria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gallardo__categoria/gallardo__categoria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gallardo__categoria.listing', {
#             'root': '/gallardo__categoria/gallardo__categoria',
#             'objects': http.request.env['gallardo__categoria.gallardo__categoria'].search([]),
#         })

#     @http.route('/gallardo__categoria/gallardo__categoria/objects/<model("gallardo__categoria.gallardo__categoria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gallardo__categoria.object', {
#             'object': obj
#         })
