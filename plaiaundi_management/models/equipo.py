# -*- coding: utf-8 -*-
from odoo import models, fields

class PlaiaundiEquipo(models.Model):
    _name = 'plaiaundi.equipo'
    _description = 'Equipamiento Informático'
    _rec_name = 'name'

    name = fields.Char(string='Nombre/Serie', required=True)
    equipment_type = fields.Selection(
        [('computer', 'Ordenador'), ('monitor', 'Pantalla'), ('other', 'Otro')],
        string='Tipo de Equipo',
        required=True
    )
    brand = fields.Char(string='Marca')
    model = fields.Char(string='Modelo')
    serial_number = fields.Char(string='Número de Serie', required=True)
    purchase_date = fields.Date(string='Fecha de Compra')
    purchase_price = fields.Float(string='Precio de Compra')
    
    aula_id = fields.Many2one(
        'plaiaundi.aula',
        string='Aula Asignada'
    )
    
    status = fields.Selection(
        [('new', 'Nuevo'), ('working', 'Funcionando'),
         ('broken', 'Averiado'), ('maintenance', 'En Mantenimiento')],
        string='Estado',
        default='working'
    )
    
    assigned_student = fields.Many2one(
        'plaiaundi.alumno',
        string='Alumno Asignado'
    )
    
    incident_ids = fields.One2many(
        'plaiaundi.mantenimiento',
        'equipment_id',
        string='Incidencias'
    )
    
    active = fields.Boolean(string='Activo', default=True)
    notes = fields.Text(string='Notas')

    def action_mark_active(self):
        for record in self:
            record.active = True

    def action_mark_inactive(self):
        for record in self:
            record.active = False
