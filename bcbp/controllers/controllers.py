# -*- coding: utf-8 -*-
from odoo import http

# class Bcbp(http.Controller):
#     @http.route('/bcbp/bcbp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bcbp/bcbp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bcbp.listing', {
#             'root': '/bcbp/bcbp',
#             'objects': http.request.env['bcbp.bcbp'].search([]),
#         })

#     @http.route('/bcbp/bcbp/objects/<model("bcbp.bcbp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bcbp.object', {
#             'object': obj
#         })