# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PlaiaundiNota(models.Model):
    _name = 'plaiaundi.nota'
    _description = 'Calificación de Alumno'

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
    subject = fields.Char(string='Asignatura', required=True)
    evaluation = fields.Selection(
        [('1', 'Primera Evaluación'), ('2', 'Segunda Evaluación'), ('3', 'Tercera Evaluación')],
        string='Evaluación',
        required=True
    )
    grade = fields.Float(
        string='Calificación',
        required=True,
        help='Escala 0-10'
    )
    date = fields.Date(string='Fecha', required=True, default=fields.Date.today)
    notes = fields.Text(string='Comentarios del Profesor')

    @api.constrains('grade')
    def _check_grade(self):
        for record in self:
            if record.grade < 0 or record.grade > 10:
                raise ValidationError('La calificación debe estar entre 0 y 10')
