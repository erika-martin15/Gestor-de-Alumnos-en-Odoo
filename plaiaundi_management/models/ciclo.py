# -*- coding: utf-8 -*-
from odoo import models, fields

class PlaiaundiCiclo(models.Model):
    _name = 'plaiaundi.ciclo'
    _description = 'Ciclo Formativo'
    _rec_name = 'name'
    
    name = fields.Char(string='Nombre del Ciclo', required=True,
                       help='Ej: SMR2, ASIR3, DAW3, DAM3')
    code = fields.Char(string='Código', required=True)
    level = fields.Selection(
        [('2', '2o Curso'), ('3', '3o Curso')],
        string='Nivel',
        required=True
    )
    students_ids = fields.One2many(
        'plaiaundi.alumno',
        'ciclo_id',
        string='Alumnos'
    )
    teachers_ids = fields.Many2many(
        'plaiaundi.profesor',
        'ciclo_profesor_rel',
        'ciclo_id',
        'profesor_id',
        string='Profesores'
    )
    classrooms_ids = fields.One2many(
        'plaiaundi.aula',
        'ciclo_id',
        string='Aulas'
    )
