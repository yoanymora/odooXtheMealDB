# -*- coding: utf-8 -*-
# from odoo import http


# class Themealdb(http.Controller):
#     @http.route('/themealdb/themealdb', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/themealdb/themealdb/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('themealdb.listing', {
#             'root': '/themealdb/themealdb',
#             'objects': http.request.env['themealdb.themealdb'].search([]),
#         })

#     @http.route('/themealdb/themealdb/objects/<model("themealdb.themealdb"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('themealdb.object', {
#             'object': obj
#         })
