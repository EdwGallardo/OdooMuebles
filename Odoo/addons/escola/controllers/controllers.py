# -*- coding: utf-8 -*-
# from odoo import http


# class EscolaGallardoAlvarez(http.Controller):
#     @http.route('/escola__gallardo__alvarez/escola__gallardo__alvarez', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/escola__gallardo__alvarez/escola__gallardo__alvarez/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('escola__gallardo__alvarez.listing', {
#             'root': '/escola__gallardo__alvarez/escola__gallardo__alvarez',
#             'objects': http.request.env['escola__gallardo__alvarez.escola__gallardo__alvarez'].search([]),
#         })

#     @http.route('/escola__gallardo__alvarez/escola__gallardo__alvarez/objects/<model("escola__gallardo__alvarez.escola__gallardo__alvarez"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('escola__gallardo__alvarez.object', {
#             'object': obj
#         })
