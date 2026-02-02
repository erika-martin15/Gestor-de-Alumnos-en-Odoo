# -*- coding: utf-8 -*-
from odoo import models, fields

class PlaiaundiMantenimiento(models.Model):
    _name = 'plaiaundi.mantenimiento'
    _description = 'Incidencia de Mantenimiento'

    equipment_id = fields.Many2one(
        'plaiaundi.equipo',
        string='Equipo',
        required=True
    )
    description = fields.Text(string='Descripción del Problema', required=True)
    reported_date = fields.Date(string='Fecha de Reporte', required=True,
                                 default=fields.Date.today)
    priority = fields.Selection(
        [('low', 'Baja'), ('medium', 'Media'), ('high', 'Alta'), ('critical', 'Crítica')],
        string='Prioridad',
        default='medium'
    )
    status = fields.Selection(
        [('open', 'Abierta'), ('in_progress', 'En Progreso'), ('resolved', 'Resuelta'), ('closed', 'Cerrada')],
        string='Estado',
        default='open'
    )
    resolved_date = fields.Date(string='Fecha de Resolución')
    solution = fields.Text(string='Solución Aplicada')
    notes = fields.Text(string='Notas')
