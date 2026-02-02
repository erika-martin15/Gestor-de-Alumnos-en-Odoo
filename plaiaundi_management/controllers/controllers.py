# -*- coding: utf-8 -*-
# from odoo import http


# class PlaiaundiManagement(http.Controller):
#     @http.route('/plaiaundi_management/plaiaundi_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plaiaundi_management/plaiaundi_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('plaiaundi_management.listing', {
#             'root': '/plaiaundi_management/plaiaundi_management',
#             'objects': http.request.env['plaiaundi_management.plaiaundi_management'].search([]),
#         })

#     @http.route('/plaiaundi_management/plaiaundi_management/objects/<model("plaiaundi_management.plaiaundi_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plaiaundi_management.object', {
#             'object': obj
#         })

