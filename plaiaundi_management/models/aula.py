# -*- coding: utf-8 -*-
from odoo import models, fields

class PlaiaundiAula(models.Model):
    _name = 'plaiaundi.aula'
    _description = 'Aula'
    _rec_name = 'name'

    name = fields.Char(string='Nombre del Aula', required=True)
    code = fields.Char(string='Código', required=True)
    location = fields.Char(string='Ubicación', required=True)
    capacity = fields.Integer(string='Capacidad')
    
    ciclo_id = fields.Many2one(
        'plaiaundi.ciclo',
        string='Ciclo Formativo',
        required=True
    )
    equipment_ids = fields.One2many(
        'plaiaundi.equipo',
        'aula_id',
        string='Equipamiento'
    )
