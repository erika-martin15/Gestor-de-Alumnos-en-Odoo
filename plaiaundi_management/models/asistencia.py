# -*- coding: utf-8 -*-
from odoo import models, fields

class PlaiaundiAsistencia(models.Model):
    _name = 'plaiaundi.asistencia'
    _description = 'Asistencia de Alumno'

    student_id = fields.Many2one(
        'plaiaundi.alumno',
        string='Alumno',
        required=True
    )
    teacher_id = fields.Many2one(
        'plaiaundi.profesor',
        string='Profesor',
        required=True
    )
    date = fields.Date(string='Fecha', required=True, default=fields.Date.today)
    status = fields.Selection(
        [('present', 'Presente'), ('absent', 'Ausente'), ('justified', 'Justificado')],
        string='Estado',
        required=True,
        default='present'
    )
    notes = fields.Text(string='Notas')
