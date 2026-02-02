# -*- coding: utf-8 -*-
from odoo import models, fields

class PlaiaundiAlumno(models.Model):
    _name = 'plaiaundi.alumno'
    _description = 'Alumno'
    _rec_name = 'name'

    name = fields.Char(string='Nombre Completo', required=True)
    email = fields.Char(string='Email Corporativo', required=True,
                        help='Formato: ik012108XXXplaiaundi.com')
    student_code = fields.Char(string='Código del Alumno', required=True)
    date_of_birth = fields.Date(string='Fecha de Nacimiento')
    gender = fields.Selection(
        [('male', 'Masculino'), ('female', 'Femenino'), ('other', 'Otro')],
        string='Género'
    )
    phone = fields.Char(string='Teléfono')
    address = fields.Text(string='Dirección')
    
    ciclo_id = fields.Many2one(
        'plaiaundi.ciclo',
        string='Ciclo Formativo',
        required=True
    )
    
    assigned_computer = fields.Many2one(
        'plaiaundi.equipo',
        string='Ordenador Asignado',
        domain=[('equipment_type', '=', 'computer')]
    )
    assigned_monitor = fields.Many2one(
        'plaiaundi.equipo',
        string='Pantalla Asignada',
        domain=[('equipment_type', '=', 'monitor')]
    )
    
    attendance_ids = fields.One2many(
        'plaiaundi.asistencia',
        'student_id',
        string='Asistencias'
    )
    grades_ids = fields.One2many(
        'plaiaundi.nota',
        'student_id',
        string='Calificaciones'
    )
    
    active = fields.Boolean(string='Activo', default=True)
    notes = fields.Text(string='Notas')

    def action_mark_active(self):
        for record in self:
            record.active = True

    def action_mark_inactive(self):
        for record in self:
            record.active = False
