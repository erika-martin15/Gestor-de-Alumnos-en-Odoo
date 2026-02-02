# -*- coding: utf-8 -*-
from odoo import models, fields

class PlaiaundiProfesor(models.Model):
    _name = 'plaiaundi.profesor'
    _description = 'Profesor'
    _rec_name = 'name'

    name = fields.Char(string='Nombre Completo', required=True)
    email = fields.Char(string='Email Corporativo', required=True,
                        help='Formato: ir012108XXplaiaundi.com')
    teacher_code = fields.Char(string='Código del Profesor', required=True)
    phone = fields.Char(string='Teléfono')
    specialization = fields.Char(string='Especialización')
    
    ciclo_ids = fields.Many2many(
        'plaiaundi.ciclo',
        'ciclo_profesor_rel',
        'profesor_id',
        'ciclo_id',
        string='Ciclos que Imparte'
    )
    
    attendance_ids = fields.One2many(
        'plaiaundi.asistencia',
        'teacher_id',
        string='Asistencias Registradas'
    )
    
    grades_ids = fields.One2many(
        'plaiaundi.nota',
        'teacher_id',
        string='Calificaciones Registradas'
    )
    
    active = fields.Boolean(string='Activo', default=True)
    notes = fields.Text(string='Notas')

    def action_mark_active(self):
        for record in self:
            record.active = True

    def action_mark_inactive(self):
        for record in self:
            record.active = False
